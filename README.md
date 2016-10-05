# The `jutge` package [![Build Status](https://travis-ci.org/jutge-org/jutge-python.svg?branch=master)](https://travis-ci.org/jutge-org/jutge-python) [![Python Versions](https://img.shields.io/pypi/v/jutge.svg)](https://pypi.python.org/pypi/jutge) [![PyPi Version](https://img.shields.io/pypi/pyversions/jutge.svg)](https://pypi.python.org/pypi/jutge)

![Logo](logo.png)

This tiny package offers a simple function to read input from
Python for problems in Jutge.org. It was built in order to offer
beginners an easy interface to read data in
[Jutge.org](https://www.jutge.org) problems.


# Installation

- Python3:
    - Install with `pip3 install jutge`.
    - Upgrade to latest version with `pip3 install --upgrade jutge`.
    - Uninstall with `pip3 uninstall jutge`.
- Python:
    - Install with `pip install jutge`.
    - Upgrade to latest version with `pip install --upgrade jutge`.
    - Uninstall with `pip uninstall jutge`.


# Usage

This package exports a `read` function that returns the next token of the
input. The type of the token must be given as a parameter: `read(int)`,
`read(float)`, `read(str)`, `read(chr)`... In the event no more tokens are available,
`read` returns `None`. Except for characters, tokens are separated by words, so that `read(str)`
returns the next word. Whitespace characters cannot be obtained.

Sample program to read two numbers and write their maximum:

```python
from jutge import read

x = read(int)
y = read(int)
if x > y:
    m = x
else:
    m = y
print(m)
```

Sample program to compute the sum of a sequence of integers:

```python
from jutge import read

s = 0
x = read(int)
while x is not None:
    s = s + x
    x = read(int)
print(s)
```


Sample program to count the number of 'A' characters in a text:

```python
from jutge import read

n = 0
c = read(chr)
while c is not None:
    if c == 'A':
        n = n + 1
    c = read(chr)
print(n)
```

Of course, you can also just import the package and prefix the `read` function with `jutge`:

```python
import jutge, math

x = jutge.read(float)
print(math.sin(x))
```



## Multiple tokens

The `read` function also admits a variable number of parameters. If no parameter
is given, it defaults to `str`. If more than one parameter is given, it returns
a list with as many tokens as requested, each of the corresponding type, filling
the list with `None` values if input is exhausted.

Sample program to compute the sum of two floats:

```python
from jutge import read

a, b = read(float, float)
print(a + b)
```

## Usage of a file stream

Additionally, the `read` function accepts a `file` keyword argument that specifies the file stream to read from. By default, `file` stands for `sys.stdin`.

Sample program to read each number from an open file:

```python
from jutge import read

with open('file.txt') as f:
    x = read(int, file=f)
    while x is not None:
        print(x)
        x = read(int, file=f)
```

Under Python3, one can use `io.StringIO` to read from strings by converting them into streams:

```Python
import io
from jutge import read

string = "21 40\n"
stream = io.StringIO(string)
x = read(int, file=stream)
y = read(int, file=stream)
print(x + y)
```

## Basic types

The `read` function supports the following basic built-in types:

- integer (`int`),
- floating point (`float`),
- character (`chr`),
- string (`str`).


## User defined types

Any type whose constructor accepts a `string` is also supported; for example `read(iter)` will yield a string iterator:

```python
from jutge import read

class mytype:
    def __init__(self, word): self.word = word
    def sayAWord(self): print(self.word)

a = read(mytype)  # a = mytype(inputstring)
print('Type name: ' + type(a).__name__)
a.sayAWord()
```

## Version

The variable `jutge.version` keeps the version of the package.


## Extra features

Additionally, when importing the `jutge` package, the maximum depth of the
Python interpreter stack is increased (using
`sys.setrecursionlimit(1000000)`). This feature helps solving some recursive
problems in Jutge.org.


## Usage warnings

- When using `read` interactively, you need to end the input with
<kbd>control</kbd> + <kbd>d</kbd> on Linux and Mac or <kbd>control</kbd> +
<kbd>z</kbd> on Windows.

- Reading many individual characters is very time consuming. If possible, try to read words and iterate through their characters. Eg:

    ```python
    # slow:
    n = 0
    c = read(chr)
    while c is not None:
        if c == 'A':
            n = n + 1
        c = read(chr)
    print(n)
      
    # faster:
    n = 0
    w = read(str)
    while w is not None:
        for c in w:
            if c == 'A':
                n = n + 1
        w = read(str)
    print(n)
    ```

# Credits

- Jordi Petit https://github.com/jordi-petit
- Albert Lobo https://github.com/llop


# License

[Apache License 2.0](LICENSE.txt)
