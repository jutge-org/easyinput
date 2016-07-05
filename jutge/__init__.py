
def tokenizer (f):
    for line in f.readlines():
        for word in line.split():
            yield word
    while True:
        yield None

files = {}

def read (*types, **kwargs):
    import sys

    if 'file' in kwargs: f = kwargs['file']
    else: f = sys.stdin

    if f not in files: files[f] = tokenizer(f)
    tokens = files[f]

    if len(types) == 0:
        token = next(tokens)
        if token is None: return None
        return token
    elif len(types) == 1:
        token = next(tokens)
        if token is None: return None
        return types[0](token)
    else:
        result = []
        for typ in types:
            token = next(tokens)
            if token is None: result.append(None)
            else: result.append(typ(token))
        return result

