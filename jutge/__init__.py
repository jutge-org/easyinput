# iterator class
class JutgeTokenizer:

    def __init__(self, stream):
        self.stream = stream
        self.typ = str
        self.words = iter('')
        self.word = None

    def __iter__(self):
        return self

    def __next__(self):
        # get next word if need be
        if self.word is None:
            self.word = next(self.words, None)
            if self.word is None:
                line = next(self.stream, '')
                self.words = iter(line.split())
                self.word = next(self.words, None)

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
