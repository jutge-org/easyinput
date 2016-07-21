# The `jutge` package [![Build Status](https://travis-ci.org/jutge-org/jutge-python.svg?branch=master)](https://travis-ci.org/jutge-org/jutge-python)

![Logo](logo.png)

This tiny package offers a simple function to read input from
Python for problems in Jutge.org. It was built in order to offer
beginners an easy interface to read data in
[Jutge.org](https://www.jutge.org) problems.


# Installation

- Python3:
    - Install with `pip3 install jutge`.
    - Upgrade to lattest version with `pip3 install jutge --upgrade`.
    - Uninstall with `pip3 uninstall jutge`.
- Python:
    - Install with `pip install jutge`.
    - Upgrade to latest version with `pip install jutge --upgrade`.
    - Uninstall with `pip uninstall jutge`.


# Description

This package exports a `read` function that returns the next token of the
input. The type of the token must be given as a parameter: `read(int)`,
`read(float)`, `read(str)`, `read(chr)`... In the event no more tokens are available,
`read` returns `None`. Except for characters, tokens are separated by words, so that `read(str)`
returns the next word. Whitespace characters cannot be obtained.

Sample program to compute the sum of a sequence of integers:

```python
from jutge import read

s = 0
x = read(int)
while x is not None:
    s += x
    x = read(int)
print(s)
```


## Multiple tokens

Function `read` also admits a variable number of parameters. If no parameter
is given, it defaults to `str`. If more than one parameter is given, it returns
a list with as many tokens as requested, each of the corresponding type, filling
with `None` values if input is exhausted.

Sample program to compute the sum of two floats:

```python
from jutge import read

a, b = read(float, float)
print(a+b)
```

Of course, you can also just import the package:

```python
import jutge

a, b = jutge.read(float, float)
print(a+b)
```

## Usage of a file descriptor

Additionally, the `read` function accepts a `file` keyword argument that specifies the file descriptor to read from. By default, `file` stands for `sys.stdin`.

Sample program to read each number from an open file:

```python
from jutge import read

with open('file.txt') as f:
    x = read(int, file=f)
    while x is not None:
        print(x)
        x = read(int, file=f)
```


## Basic types

The `read`function supports the following basic built-in types:

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

## Extra features

Additionally, when importing the `jutge` package, the maximum depth of the
Python interpreter stack is increased (using
`sys.setrecursionlimit(1000000)`). This feature helps solving some recursive
problems in Jutge.org.



# Warning

When using `read` interactively, you need to end the input with
<kbd>control</kbd> + <kbd>d</kbd> on Linux and Mac or <kbd>control</kbd> +
<kbd>z</kbd> on Windows.
