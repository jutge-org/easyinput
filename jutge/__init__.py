"""
jutge package for alternative input handling.
see https://github.com/jutge-org/jutge-python
"""

import sys
from future.builtins import int  # for Python2 compatibility
from jutge.utils import kwd_only

__all__ = ['read', 'keep_reading']  # Specify what to import with *
version = "1.8"  # current version


class JutgeTokenizer:
    """Iterator class for parsing and converting tokens
    from a stream."""

    def __init__(self, stream):
        self.stream = stream
        self.typ = str
        self.words_in_line = None
        self.word = None
        self.worditer = None
        self.wordidx = None
        self.wordlen = None
        self.__init_next_line()
        self.__init_next_word()

    def __iter__(self):
        return self

    def __init_next_line(self):
        """Find next non-empty line"""
        for line in self.stream:
            line = line.strip()
            if line:
                self.words_in_line = iter(line.split())
                return
        raise EOFError

    def __next_word(self):
        """Find next non-empty word"""
        word = next(self.words_in_line, None)
        if word is None:
            self.__init_next_line()
            word = next(self.words_in_line)
        return word

    def __init_next_word(self):
        """Init next word and corresponding variables"""
        self.word = self.__next_word()
        self.worditer = iter(self.word)
        self.wordidx = 0
        self.wordlen = len(self.word)

    def __next__(self):
        """Find next token using current `self.type`."""
        # get next word if need be
        if self.word is None:
            self.__init_next_word()

        # return whatever
        if self.typ == chr:
            value = next(self.worditer)
            self.wordidx += 1
            if self.wordidx == self.wordlen:  # If all chars have been read
                self.word = None
        else:
            value = self.typ(self.word[self.wordidx:])
            self.word = None
        return value

    def next(self):
        """For Python2 compatibility purposes."""
        return self.__next__()

    def nexttoken(self, typ=str):
        """Get next token as the specified type."""
        self.typ = typ
        return next(self)


def StdIn():
    """
    Generator that emulates `sys.stdin`. Uses `input()` builtin
    rather than directly using sys.stdin to allow usage within an
    interactive session.
    """
    while True:
        yield input()


tokenizers = {}  # dictionary of open tokenizer objects
__StdIn = StdIn()


@kwd_only(file=__StdIn, amount=1)  # Python 2 compatibility
def read(*types, **kwargs):
    """
    Py3 signature: `read(*types, file=files['stdin'], amount: int = 1) -> iter`
    This function returns one or more tokens converted to
    the types specified by *types.
    This is the main function in the module.
    """
    tokens, amount = __unpack(**kwargs)
    return __read(tokens, amount, *types)


@kwd_only(file=__StdIn, amount=1)  # Python 2 compatibility
def keep_reading(*types, **kwargs):
    """
    Py3 signature: `keep_reading(*types, file=files['stdin']) -> iter`
    Generator that yields converted tokens while the
    stream is not empty and the tokens can be converted
    to the specified types.
    """
    try:
        tokens, amount = __unpack(**kwargs)
        while True:
            yield __read(tokens, amount, *types)
    except ValueError:
        return
    except EOFError:
        return


def __read(tokens, amount, *types):
    if len(types) <= 1:
        typ = types[0] if types else str
        if amount == 1:  # Return single value
            return tokens.nexttoken(typ)
        else:  # Return generator of type-homogeneous values
            tokens.typ = typ  # Set fixed type for efficiency
            return (next(tokens) for _ in range(amount))
    else:  # Return generator of type-heterogenous values
        return (tokens.nexttoken(typ) for _ in range(amount) for typ in types)


def __unpack(**kwargs):
    file, amount = kwargs['file'], kwargs['amount']
    if not isinstance(amount, int):
        raise TypeError("Expected integer amount")
    if not amount > 0:
        raise ValueError("Expected positive amount")
    if file not in tokenizers:
        tokenizers[file] = JutgeTokenizer(file)
    tokens = tokenizers[file]

    return tokens, amount


sys.setrecursionlimit(1000000)  # hack to get more stack size
