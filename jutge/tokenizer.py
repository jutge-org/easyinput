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
        self.words_in_line = []
        self._wordidx = 0
        self._word = ''
        self._charidx = 0

    @property
    def word(self):
        """Gets current word"""
        if self._charidx >= len(self._word):
            self._wordidx += 1
            self._charidx = 0
        if self._wordidx >= len(self.words_in_line):
            self._init_next_line()
        self._word = self.words_in_line[self._wordidx]
        return self._word

    def get_nonempty_line(self):
        """Returns next non-empty line in stream"""
        for line in self.stream:
            line = line.strip()
            if line:
                return line
        raise EOFError

    def _init_next_line(self):
        """Initialize next line and associated variables"""
        self.words_in_line = self.get_nonempty_line().split()
        self._wordidx = 0

    def nexttoken(self, typ=str):
        """Get next token as the specified type."""
        try:
            # return whatever
            if typ == chr:
                value = self.word[self._charidx]
                self._charidx += 1
            else:
                value = typ(self.word[self._charidx:])
                self._wordidx += 1
                self._charidx = 0
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


@kwd_only(file=_StdIn, amount=1, as_list=True)  # Python 2 compatibility
def read(*types, **kwargs):
    """
    Py3 signature:
        `read(*types, file:iter=_StdIn, amount:int=1, as_list:bool=True)`
    This function returns one or more tokens converted to
    the types specified by *types.
    This is the main function in the module.
    """
    tokens, amount, as_list = _get_tokenizer(kwargs), _get_amount(kwargs), kwargs['as_list']
    method, args = _select_method(tokens, types, amount, as_list)
    return method(*args)


@kwd_only(file=_StdIn, amount=1)  # Python 2 compatibility
def read_many(*types, **kwargs):
    """
    Py3 signature:
        `read_many(*types, file:iter=_StdIn, amount:int=1)`
    Generator that yields converted tokens while the
    stream is not empty and the tokens can be converted
    to the specified types.
    """
    previous_eof_mode = _EOFMode
    set_eof_handling(EOFModes.RaiseException)
    try:
        tokenizer, amount = _get_tokenizer(kwargs), _get_amount(kwargs)
        method, args = _select_method(tokenizer, types, amount, True)
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


def _get_tokenizer(kwargs):
    """Helper function intended for internal use. Gets open tokenizer object."""
    file = kwargs['file']
    if file not in _tokenizers:
        _tokenizers[file] = JutgeTokenizer(file)
    return _tokenizers[file]


def _get_amount(kwargs):
    """Helper function intended for internal use. Checks validity of `amount` kwarg."""
    amount = kwargs['amount']
    if not isinstance(amount, int):
        raise TypeError("Expected integer amount")
    if not amount >= 0:
        raise ValueError("Expected non-negative amount")
    return amount


def _select_method(tokens, types, amount, as_list):
    """
    Intended for internal use. Helper function for `read` and `read_many`.
    Selects the specific method to be used based on type/token amount.
    """

    if len(types) <= 1 and amount <= 1:
        method, args, as_list = tokens.nexttoken, types, False
    else:
        method, args = tokens.multiple_tokens, (amount,) + types

    return (lambda *x: list(method(*x))) if as_list else method, args


sys.setrecursionlimit(1000000)  # hack to get more stack size
