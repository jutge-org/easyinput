
import sys

def tokenizer():
    for line in sys.stdin.readlines():
        for word in line.split():
            yield word
    while True:
        yield None

tokens = tokenizer()

def read (typ = str):
    token = next(tokens)
    if token is None: return None
    return typ(token)

