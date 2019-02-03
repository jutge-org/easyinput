import enum
import sys

from future.builtins import int  # for Python2 compatibility

from jutge.utils import kwd_only, StdIn


class EOFModes(enum.Enum):
    """Enum of handling modes for end-of-input"""
    ReturnNone = 0
    RaiseException = 1


_EOFMode = EOFModes.ReturnNone  # default handling mode


def set_eof_handling(mode):
    """EOF mode frontend setter"""
    global _EOFMode
    if not isinstance(mode, EOFModes):
        raise TypeError("Invalid EOF mode specifier")
    _EOFMode = mode


class JutgeTokenizer(object):
    """Iterator class for parsing and converting tokens
    from a stream."""

    class InputTypeError(ValueError):
        """Custom exception for invalid literals for given type"""
        pass

    def __init__(self, stream):
        self.stream = stream
        self.words_in_line = iter("")
        self.word = None
        self.wordidx = 0
        self.wordlen = 0

    @property
    def word(self):
        """Gets current word"""
        if self._word is None or self.wordidx == self.wordlen:
            return None
        return self._word[self.wordidx:]

    @word.setter
    def word(self, value):
        self._word = value

    def get_line(self):
        """Returns next non-empty line in stream"""
        for line in self.stream:
            line = line.strip()
            if line:
                return line
        raise EOFError

    def _init_next_line(self):
        """Initialize line iterator for next line"""
        self.words_in_line = iter(self.get_line().split())

    def _init_next_word(self):
        """Get next non-empty word and  init corresponding variables"""
        word = next(self.words_in_line, None)
        if word is None:
            self._init_next_line()
            word = next(self.words_in_line)
        self.word = word
        self.wordidx = 0
        self.wordlen = len(word)

    def nexttoken(self, typ=str):
        """Get next token as the specified type."""
        try:
            # get next word if need be
            if self.word is None:
                self._init_next_word()

            # return whatever
            if typ == chr:
                value = self.word[0]
                self.wordidx += 1
            else:
                value = typ(self.word)
                self.word = None
            return value

        except EOFError:
            if _EOFMode is EOFModes.RaiseException:
                raise EOFError("Tried to read when end of input was reached")
            elif _EOFMode is EOFModes.ReturnNone:
                return None
        except ValueError:
            raise JutgeTokenizer.InputTypeError("Unable to parse '{}' as {}".format(self.word, typ))

    def multiple_tokens(self, amount, type1=str, *types):
        """Returns generator of tokens as specified types"""
        for _ in range(amount):
            yield self.nexttoken(type1)
            for typ in types:
                yield self.nexttoken(typ)


_tokenizers = {}  # dictionary of open tokenizer objects
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
def read_while(*types, **kwargs):
    """
    Py3 signature:
        `read_while(*types, file:iter=_StdIn, amount:int=1, astuple:bool=False)`
    Generator that yields converted tokens while the
    stream is not empty and the tokens can be converted
    to the specified types.
    """
    previous_eof_mode = _EOFMode
    set_eof_handling(EOFModes.RaiseException)
    try:
        tokens, amount, astuple = __unpack_and_check(**kwargs)
        method, args = __select_method(tokens, types, amount, astuple)
        while True:
            yield method(*args)
    except JutgeTokenizer.InputTypeError:
        return
    except EOFError:
        return
    finally:
        set_eof_handling(previous_eof_mode)


@kwd_only(file=_StdIn)
def get_line(**kwargs):
    tokens, _, _ = __unpack_and_check(**kwargs)
    return tokens.get_line()


def __unpack_and_check(**kwargs):
    """
    Intended for internal use only. Helper function for `read` and `read_while`.
    Gets relevant kwrags and does whatever type/value checking needs to be made.
    """

    file = kwargs.get('file', None)
    amount = kwargs.get('amount', None)
    astuple = kwargs.get('astuple', None)
    if amount is not None:
        if not isinstance(amount, int):
            raise TypeError("Expected integer amount")
        if not amount >= 0:
            raise ValueError("Expected non-negative amount")
    if file not in _tokenizers:
        _tokenizers[file] = JutgeTokenizer(file)
    tokens = _tokenizers[file]

    return tokens, amount, astuple


def __select_method(tokens, types, amount, astuple):
    """
    Intended for internal use only. Helper function for `read` and `read_while`.
    Selects the specific method to be used based on type/token amount.
    """

    if len(types) <= 1 and amount <= 1:
        method, args = tokens.nexttoken, types
    else:
        method, args = tokens.multiple_tokens, (amount,) + types

    return (lambda *x: tuple(method(*x))) if astuple else method, args


sys.setrecursionlimit(1000000)  # hack to get more stack size
