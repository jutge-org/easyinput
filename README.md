# Package jutge

This tiny package offers a simple function to read input from Python for problems in Jutge.org.

# Installation

Simply install with `pip3 install jutge` (Python3) or `pip install jutge` (Python). It can
be removed with `pip(3) uninstall jutge`.

# Description

This package exports a `read` function that returns the next token of the
input. The type of the token must be given as a parameter: `read(int)`,
`read(float)`, `read(str)`... In the event no more tokens are available,
`read` returns `None`. Tokens separate input by words, so that `read(str)`
returns the next word.

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

# Warning

When using `read` interactively, you need to end the input with <kbd>control</kbd> + <kbd>d</kbd> on Linux and Mac
or <kbd>control</kbd> + <kbd>z</kbd> on Windows.
