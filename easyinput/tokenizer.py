import enum
import sys

from future.builtins import int  # for Python2 compatibility

from easyinput.utils import kwd_only, StdIn


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


def _handle_eof():
    """
    Internal function called when EOF is encountered.
    Behaves according to global EOF mode
    """
    if _EOFMode is EOFModes.RaiseException:
        raise EOFError("Tried to read when end of input was reached")
    elif _EOFMode is EOFModes.ReturnNone:
        return None


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
        self.reached_eof = False

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

    def get_line(self):
        self._wordidx = len(self.words_in_line)
        for line in self.stream:
            return line
        raise EOFError

    def get_nonempty_line(self):
        """Returns next non-empty stripped line in stream"""
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
        if self.reached_eof:
            return _handle_eof()  # shortcut when no more input is available
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
            self.reached_eof = True
            return _handle_eof()
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
    tokenizer, amount = _get_tokenizer(kwargs), _get_amount(kwargs)
    method, args = _select_method(tokenizer, types, amount, True)

    try:
        while True:
            yield method(*args)
    except (JutgeTokenizer.InputTypeError, EOFError):
        return
    finally:
        set_eof_handling(previous_eof_mode)


@kwd_only(file=_StdIn, rstrip=True, skip_empty=False)
def read_line(**kwargs):
    """
    Gets next line in input. If `skip_empty` is True, only lines with
    at least one non-whitespace character are returned.
    :return: str
    """
    tokenizer = _get_tokenizer(kwargs)
    skip_empty, rstrip = kwargs['skip_empty'], kwargs['rstrip']
    try:
        if skip_empty:
            return tokenizer.get_nonempty_line()
        line = tokenizer.get_line()
        return line.rstrip('\r\n') if rstrip else line
    except EOFError:
        return _handle_eof()


@kwd_only(file=_StdIn, rstrip=True, skip_empty=False)
def read_many_lines(**kwargs):
    """
    Generates iterable sequence of the lines in the input (that haven't been read).
    If `skip_empty` is True, only lines with at least one non-whitespace character
    are yielded.
    :return: str
    """
    tokenizer = _get_tokenizer(kwargs)
    skip_empty, rstrip = kwargs['skip_empty'], kwargs['rstrip']
    try:
        if skip_empty:
            while True:
                yield tokenizer.get_nonempty_line()
        else:
            while True:
                line = tokenizer.get_line()
                yield line.rstrip('\r\n') if rstrip else line
    except EOFError:
        return


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
