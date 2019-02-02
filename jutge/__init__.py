"""
jutge package for alternative input handling.
see https://github.com/jutge-org/jutge-python
"""

import sys
from future.builtins import int, input  # for Python2 compatibility
from jutge.utils import kwd_only

__all__ = ['read', 'keep_reading']  # Specify what to import with *
version = "2.0"  # current version


class JutgeTokenizer:
    """Iterator class for parsing and converting tokens
    from a stream."""

    class InputTypeError(TypeError):
        """Custom exception for invalid literals for given type"""
        pass

    def __init__(self, stream):
        self.stream = stream
        self.words_in_line = iter("")
        self.word = None
        self.worditer = None
        self.wordidx = 0
        self.wordlen = 0

    @property
    def word(self):
        return self._word[self.wordidx:] if self._word else None

    @word.setter
    def word(self, value):
        self._word = value

    def __init_next_line(self):
        """Find next non-empty line"""
        for line in self.stream:
            line = line.strip()
            if line:
                self.words_in_line = iter(line.split())
                return
        raise EOFError

    def __init_next_word(self):
        """Get next non-empty word and  init corresponding variables"""
        word = next(self.words_in_line, None)
        if word is None:
            self.__init_next_line()
            word = next(self.words_in_line)
        self.word = word
        self.worditer = iter(self.word)
        self.wordidx = 0
        self.wordlen = len(self.word)

    def nexttoken(self, typ=str):
        """Get next token as the specified type."""
        # get next word if need be
        if self.word is None:
            self.__init_next_word()

        # return whatever
        if typ == chr:
            value = next(self.worditer)
            self.wordidx += 1
            if self.wordidx == self.wordlen:  # If all chars have been read
                self.word = None
        else:
            try:
                value = typ(self.word[self.wordidx:])
                self.word = None
            except ValueError:
                raise JutgeTokenizer.InputTypeError
        return value

    def multiple_tokens(self, amount, type1=str, *types):
        """Return generator of type-heterogenous values"""
        for _ in range(amount):
            yield self.nexttoken(type1)
            for typ in types:
                yield self.nexttoken(typ)


def StdIn():
    """
    Generator that emulates `sys.stdin`. Uses `input()` builtin
    rather than directly using sys.stdin to allow usage within an
    interactive session.
    """
    while True:
        yield input()


tokenizers = {}  # dictionary of open tokenizer objects
_StdIn = StdIn()


@kwd_only(file=_StdIn, amount=1, astuple=False)  # Python 2 compatibility
def read(*types, **kwargs):
    """
    Py3 signature:
        `read(*types, file:iter=_StdIn, amount:int=1, astuple:bool=False)`
    This function returns one or more tokens converted to
    the types specified by *types.
    This is the main function in the module.
    """
    tokens, amount, astuple = __unpack_and_check(**kwargs)
    method, args = __select_method(tokens, types, amount, astuple)
    return method(*args)


@kwd_only(file=_StdIn, amount=1, astuple=False)  # Python 2 compatibility
def keep_reading(*types, **kwargs):
    """
    Py3 signature:
        `keep_reading(*types, file:iter=_StdIn, amount:int=1, astuple:bool=False)`
    Generator that yields converted tokens while the
    stream is not empty and the tokens can be converted
    to the specified types.
    """
    try:
        tokens, amount, astuple = __unpack_and_check(**kwargs)
        method, args = __select_method(tokens, types, amount, astuple)
        while True:
            yield method(*args)
    except JutgeTokenizer.InputTypeError:
        return
    except EOFError:
        return


def __unpack_and_check(**kwargs):
    """
    Intended for internal use only. Helper function for `read` and `keep_reading`.
    Gets relevant kwrags and does whatever type/value checking needs to be made.
    """

    file, amount, astuple = kwargs['file'], kwargs['amount'], kwargs['astuple']
    if not isinstance(amount, int):
        raise TypeError("Expected integer amount")
    if not amount >= 0:
        raise ValueError("Expected nonnegative amount")
    if file not in tokenizers:
        tokenizers[file] = JutgeTokenizer(file)
    tokens = tokenizers[file]

    return tokens, amount, astuple


def __select_method(tokens, types, amount, astuple):
    """
    Intended for internal use only. Helper function for `read` and `keep_reading`.
    Selects the specific method to be used based on type/token amount.
    """

    if len(types) <= 1 and amount <= 1:
        method, args = tokens.nexttoken, types
    else:
        method, args = tokens.multiple_tokens, (amount,) + types

    return (lambda *x: tuple(method(*x))) if astuple else method, args


sys.setrecursionlimit(1000000)  # hack to get more stack size
