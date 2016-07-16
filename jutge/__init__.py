# iterator class
class JutgeTokenizer:

    def __init__(self, stream):
        self.stream = stream
        self.typ = str
        self.words = iter('')
        self.word = None

    def __iter__(self):
        return self

    # find next non-empty line
    def __nextline__(self):
        line = next(self.stream, None)
        if line is not None: line = line.strip()
        while line == '':
            line = next(self.stream, None)
            if line is not None: line = line.strip()
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
    
    # find next token
    def __next__(self):
        # get next word if need be
        if self.word is None: self.word = self.__nextword__()

        # return nothing if there's no input
        if self.word is None: return None

        # otherwise return whatever
        if self.typ == chr: 
            value, self.word = self.word[0], self.word[1:]
            if self.word == '': self.word = None
            return value
        else:
            value = self.typ(self.word)
            self.word = None
            return value

    # python2 compatible
    def next(self): return self.__next__()

    # call this function to get next token as the specified type
    def nexttoken(self, typ = str):
        self.typ = typ
        return next(self)


# read method
files = {}
def read(*types, **kwargs):
    import sys

    if 'file' in kwargs: f = kwargs['file']
    else: f = sys.stdin

    if f not in files: files[f] = JutgeTokenizer(f)
    tokens = files[f]

    if len(types) == 0:
        return tokens.nexttoken()
    elif len(types) == 1:
        return tokens.nexttoken(types[0])
    else:
        return [tokens.nexttoken(typ) for typ in types]
