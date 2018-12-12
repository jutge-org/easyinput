# see https://github.com/jutge-org/jutge-python

import sys


# current version
version = "1.8"


# iterator class
class JutgeTokenizer:

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

    # find next non-empty line
    def __nextline__(self):
        line = next(self.stream, None)
        if line is not None:
            line = line.strip()
        while line == '':
            line = next(self.stream, None)
            if line is not None:
                line = line.strip()
        return line

    # find next non-empty word
    def __nextword__(self):
        word = next(self.words, None)
        if word is None:
            line = self.__nextline__()
            if line is not None:
                self.words = iter(line.split())
                word = next(self.words, None)
        return word

    # init next word data variables
    def __initnextword__(self):
        self.word = self.__nextword__()
        if self.word is not None:
            self.worditer = iter(self.word)
            self.wordidx = 0
            self.wordlen = len(self.word)

    # find next token
    def __next__(self):
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

    # python2 compatible
    def next(self):
        return self.__next__()

    # call this function to get next token as the specified type
    def nexttoken(self, typ=str):
        self.typ = typ
        return next(self)


class StdIn:

    # Internal implementation to allow singleton pattern:
    class __StdIn:
        def __next__(self):
            try:
                return input()
            except EOFError:
                return None

    # Singleton instance:
    instance = None

    def __new__(cls):
        if StdIn.instance is None:
            StdIn.instance = StdIn.__StdIn()
        return StdIn.instance  # Use singleton

    def __next__(self):
        return StdIn.instance.__next__()


# read method
files = {}


def read(*types, file=StdIn(), amount: int = 1):
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
        return (tokens.nexttoken(typ) for typ in types)


# hack to get more stack size
sys.setrecursionlimit(1000000)
