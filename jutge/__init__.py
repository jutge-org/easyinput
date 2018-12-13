"""
jutge package for alternative input handling.
see https://github.com/jutge-org/jutge-python
"""

import sys

__all__ = ['read', 'keep_reading']  # Specify what to import with *
version = "1.8"  # current version


class JutgeTokenizer:
    """Iterator class for parsing and converting tokens
    from a stream."""

    def __init__(self, stream):
        self.stream = stream
        self.typ = str
        self.words = iter('')
        self.word = None
        self.worditer = None
        self.wordidx = 0
        self.wordlen = 0

    def __iter__(self):
        return self

    def __nextline__(self):
        """Find next non-empty line"""
        for line in self.stream:
            line = line.strip()
            if line:
                return line
        return None

    def __nextword__(self):
        """Find next non-empty word"""
        word = next(self.words, None)
        if word is None:
            line = self.__nextline__()
            if line is not None:
                self.words = iter(line.split())
                word = next(self.words, None)
        return word

    def __initnextword__(self):
        """Init next word and corresponding variables"""
        self.word = self.__nextword__()
        if self.word is not None:
            self.worditer = iter(self.word)
            self.wordidx = 0
            self.wordlen = len(self.word)

    def __next__(self):
        """Find next token using current `self.type`."""
        # get next word if need be
        if self.word is None:
            self.__initnextword__()

        # return nothing if there's no input
        if self.word is None:
            return None

        # otherwise return whatever
        if self.typ == chr:
            value = next(self.worditer)
            self.wordidx += 1
            if self.wordidx == self.wordlen:
                self.word = None
            return value
        else:
            value = self.typ(self.word[self.wordidx:])
            self.word = None
            return value

    def next(self):
        """For Python2 compatibiliti purposes."""
        return self.__next__()

    def nexttoken(self, typ=str):
        """Get next token as the specified type."""
        self.typ = typ
        return next(self)


def StdIn() -> iter:
    """
    Generator that emulates `sys.stdin`. Uses `input()` builtin
    rather than directly using sys.stdin to allow usage within an
    interactive session.
    """
    try:
        while True:
            yield input()
    except EOFError:
        return


files = {"stdin": StdIn()}  # dictionary of open files


def read(*types, file=files["stdin"], amount: int = 1):
    """
    This function returns one or more tokens converted to
    the types specified by *types.
    This is the main function in the module.

    :param types: sequence of callable types
    :param file: stream from which to read; has to be an
        iterable object, with `__next__` returning a string
    :param amount: repeat reading of *types by this amount
    :return: either a single value or a generator iterator
        with each of the tokens converted to the appropriate type
    """

    if not isinstance(amount, int):
        raise TypeError("Expected integer amount")
    if not amount > 0:
        raise ValueError("Expected positive amount")
    if file not in files:
        files[file] = JutgeTokenizer(file)
    tokens = files[file]

    if len(types) <= 1:
        typ = types[0] if types else str
        if amount == 1:
            return tokens.nexttoken(typ)
        else:
            return (tokens.nexttoken(typ) for _ in range(amount))
    else:
        return (tokens.nexttoken(typ) for typ in types for _ in range(amount))


def keep_reading(*types, file=files["stdin"]):
    """
    Generator that yields converted tokens while the
    stream is not empty and the tokens can be converted
    to the specified types.

    Effective signature is the same as `jutge.read`.
    """

    try:
        values = read(*types, file=file)
        while values is not None:
            yield values
            values = read(*types, file=file)
    except ValueError:
        return


sys.setrecursionlimit(1000000)  # hack to get more stack size
