
import sys

def tokenizer():
    for line in sys.stdin.readlines():
        for word in line.split():
            yield word
    while True:
        yield None

tokens = tokenizer()

def read (*types):
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

