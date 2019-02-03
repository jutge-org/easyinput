# The `jutge` package 
[![Build Status](https://travis-ci.org/jutge-org/jutge-python.svg?branch=master)](https://travis-ci.org/jutge-org/jutge-python) [![Coverage Status](https://coveralls.io/repos/github/jutge-org/jutge-python/badge.svg?branch=master)](https://coveralls.io/github/jutge-org/jutge-python?branch=master) [![Python Versions](https://img.shields.io/pypi/v/jutge.svg)](https://pypi.python.org/pypi/jutge) [![PyPi Version](https://img.shields.io/pypi/pyversions/jutge.svg)](https://pypi.python.org/pypi/jutge)

![Logo](logo.png)

This tiny package offers a simple interface to read input from
stdin, files, and other `io` streams. It was built in order to offer
beginners an easy interface to read data in
[Jutge.org](https://www.jutge.org) problems. The behaviour of the
reading functions mimic `C++`'s `cin` input stream.

1. [Installation](#installation)
1. [Basic usage](#basic-usage)
    1. [`read`](#read)
    2. [`read_while`](#read_while)
    3. [`get_line`](#get_line)
    3. [Multiple tokens](#multiple-tokens)
    3. [Keyword arguments](#keyword-arguments)
    3. [Specifying the file stream](#specifying-the-file-stream)
    3. [Basic types](#basic-types)
    3. [User defined types](#user-defined-types)
1. [Full reference](#full-reference)
    1. [Interface](#interface)
    2. [Extra features](#extra-features)
    3. [Version](#version)
1. [Credits](#credits)
1. [License](#license)

# Installation

- Python3:
    - Install with `pip3 install jutge`.
    - Upgrade to latest version with `pip3 install --upgrade jutge`.
    - Uninstall with `pip3 uninstall jutge`.
- Python:
    - Install with `pip install jutge`.
    - Upgrade to latest version with `pip install --upgrade jutge`.
    - Uninstall with `pip uninstall jutge`.


# Basic usage

There are three main functions available to the user: `read`, `read_while` and `get_line`. All three of them can be imported at once by using the "import all" syntax:

```python
from jutge import *

read()
read_while()
get_line()
```

Of course, you can also import the whole `jutge` namespace and 
prefix each function name with `jutge`:
```python
import jutge

jutge.read()
jutge.read_while()
jutge.get_line()
```


## `read` 
The `read` function returns the next token in the
input. The type of the token must be given as a parameter: `read(int)`,
`read(float)`, `read(str)`, `read(chr)`... Except for characters, tokens are 
separated by whitespace, so that `read(str)` returns the next single word. 
Whitespace characters cannot be obtained.

If no type is specified&mdash;i.e., calling `read()`&mdash;it defaults to `str`.

-----

**Example** <br>
Sample program to read two numbers and write their maximum:

```python
from jutge import read

x = read(int)
y = read(int)
print(max(x, y))
```

**Input**:
````text
    2
            -5
````

**Output**: `2`

----

In the event no more tokens are available,
`read` returns `None`, as default behaviour&mdash;see 
[_EOF handling modes_](#eof-handling-modes) for more details. 

-----

**Example**

```python
from jutge import read

print(read())
print(read())
```

**Input**: `hello`

**Output**: `None`

----

## `read_while`

`read_while` is a function that reads tokens as long as it can&mdash;
i.e., while there still are tokens (of the requested type) to be read. 
It has the same signature as `read`; it takes one ([or more](#multiple-tokens)) 
types as arguments.

When called it returns a generator that can be iterated through
with a `for` loop; see the examples below.

-----

**Example** <br>
The following script showcases the behaviour of `read_while`.
The `for` loop iterates though all integers in the input
(until it encounters something that isn't an integer,
or there is nothing else to be read) and prints each of
those numbers squared.

Finally, a string is read, to show that the rest
of the input is still available to be read.

```python
from jutge import read_while, read

for num in read_while(int):
    print(num**2)

print(read())  # Should print 'hello'
```

**Input**: 
```text
    2 3
    
4
5
    -1

12 hello

goodbye
```

**Output**: 
```text
4
9
16
25
1
144
hello
```

----

Since `read_while` returns a generator, it does not consume all
the input beforehand; rather, each token is fetched "on-demand"
at each iteration. Thus, the loop can be exited at any time. 
See the following example.

----

**Example**

```python
from jutge import read_while, read

print("Try to guess my number!")
for num in read_while(int):
    if num == 42:
        print("Correct! You guessed it!")
        break
    print("{} is incorrect!".format(num))

x, y = read(int), read(int)
print("{} + {} = {}".format(x, y, x + y))  # Should print '5 + 2 = 7'
```

**Input**: 
```text
7
3
11
5
81
42
5
2
```

**Output**: 
```text
Try to guess my number!
7 is incorrect!
3 is incorrect!
11 is incorrect!
5 is incorrect!
81 is incorrect!
Correct! You guessed it!
5 + 2 = 7
```

----

**Example**

Get the sum of a sequence of integers in the input.

```python
from jutge import read_while

print(sum(num for num in read_while(float)))
```

**Input**: 
```text
3.14 6.28 0.333
12 100 -51
```

**Output**: `70.753`


## `get_line`

This function takes no positional arguments. It returns the next
non-empty line in the input stream, stripped (i.e., without
leading and trailing whitespace characters).

----

**Example**

```python
from jutge import get_line, read

print(read())
print(get_line())
```

**Input**

```text
Hi, I'm a line
Hello world!
```

**Output**

```text
Hi,
Hello world!
```

----


## Multiple tokens

Both `read` and `read_while` support specifying more than one type, 
as in `read(int, chr)`. 

In `read`'s case, this usage returns
an iterable sequence&mdash;see [here](#as-list) for more details&mdash;of 
tokens, one for each type requested, respecting their order. 
For example, `read(int, chr, int)` will return a
sequence containing an `int`, a `chr`, and an `int`, *in that order*.

-----

**Example** <br>
Reading more than one token at once:

```python
from jutge import read

x, y = read(chr, int)
print(repr(x), type(x))
print(repr(y), type(y))

z, w = read(int, int)
print(z*w)
```

**Input**: `D3 4 2`

**Output**:
```text
'D' <class 'str'>
3 <class 'int'>
8
```

----

In this regard, `read_while` behaves exactly like before.
Each iteration through the generator yields
the equivalent of what would be obtained by calling
`read` with the same arguments.

That is, the following two loops are (almost) equivalent.

```python
for char, num in read_while(chr, int):
    pass  # Code goes here
```

```pythonstub
char, num = read(chr, int)
while char is not None and num is not None:
    pass  # Code goes here
    char, num = read(chr, int)
```

The only difference is that `read_while` will automatically
stop when subsequent input does not match the desired types,
whilst the second, "manual", loop, will stop with a `ValueError`.

> **Note**: be careful when using `read_while` with heterogeneous 
> types. It *will* stop when it encounters input that don't match
> the types, but those tokens will be "consumed", since right now
> there is no backtracking implemented.

## Keyword arguments

### `amount`

Both `read` and `read_while` take the optional keyword-argument
`amount`. It specifies the amount of times to "concatenate" the
requested types. I.e., `read(int, amount=4)` is equivalent to
`read(int, int, int, int)`.

It is useful when you need to read a large (but fixed) number
of tokens, as in `read(int, amount=1000)`.

It is compatible with heterogeneous types. I.e., 
`read(str, int, amount=2)` is equivalent to `read(str, int, str, int)`.

### `as_list` <a name="as-list"></a>

By default, when `read` is [called with multiple types](#multiple-tokens),
it returns a `list` with the requested tokens. If, for some reason, you
don't need implicit conversion to a `list`, `read` can return a
generator instead. This is achieved by passing `as_list=False`, as in
`read(float, amount=10000, as_list=False)`.

This has the advantage of avoiding unnecessary iteration to create the
list and copy the tokens into it. For example, you could use it to create
a large `numpy` array: 

```python
import numpy as np
from jutge import read

arr = np.array(read(float, amount=1000000, as_list=False))
```

In the previous block of code, only one iteration through all of 
the tokens takes place&mdash;the one to fill the `np.array`&mdash;
whilst if `as_list` were set to
`False`, two iterations would take place: one to fill the list, and
another to fill the array.

Keep in mind that the generator returned by `read` when `as_list` is
set to `True` *does not consume any input until you iterate through it*.
This is the reason for which `read_while` does **not** support this
keyword argument: it *must* consume input in order to discern
whether it should keep going or not, so it always returns 
multiple-token queries as lists.

### `file`

See [*Specifying the file stream*](#specifying-the-file-stream).

## Specifying the file stream

All three functions accept a `file` keyword argument that specifies 
the file stream to read from, as a `file` object 
or other `io` stream object. It defaults to the
standard input stream (as defined by the `input()` built-in).

----

**Example** <br>
Read each number from an open file:

```python
from jutge import read_while

with open('file.txt') as f:
    for num in read_while(int, file=f):
        print(num)
```

**Input (`file.txt`)**:

```text
1   2

  3     4
 
5
6
```

**Output**:

```text
1
2
3
4
5
6
```

----

One can use `io.StringIO` to read from strings by converting them into 
streams, as the following example shows.

---

**Example**

```python
import io
from jutge import read

string = "21 40\t"
stream = io.StringIO(string)
x, y = read(int, int, file=stream)
print(x + y)
```

**Output**: `41`

---

> **Note**: In Python 2.x, one must use unicode literals to be able
> to use `io.StringIO`, by including the line 
> ```python
> from __future__ import unicode_literals
> ```
> at the top of the module, or by writing string literals with
> the 'u' prefix: `u"I'm a unicode string"`.

### Reading from an interactive console session

As of version `2.0`, the standard input stream has been made to 
work with the `input()` built-in, which means everything
also works in interactive console sessions.

Keep in mind that to signal end of input you will have to enter
<kbd>control</kbd> + <kbd>d</kbd> on Linux and Mac or 
<kbd>control</kbd> + <kbd>z</kbd> on Windows.

## Basic types

The `read` function supports the following basic built-in types:

- integer (`int`),
- floating point (`float`),
- character (`chr`),
- string (`str`).


## User defined types

Any type whose constructor accepts a string is also supported; 
for example `read(iter)` will return a string iterator.


---
**Example** <br>
Read an instance of a custom class whose constructor accepts a string,
and saves an uppercase copy of the string:

```python
from jutge import read

class MyType:
    def __init__(self, word): 
        self.word = word.upper()
    
    def say_word(self): 
        print(self.word)

a = read(MyType)  # a = MyType(<input string>)
a.say_word()
```

**Input**: `hello`

**Output**: `HELLO`

---

# Full reference

## Interface

- *(function)* `jutge.read(*types, amount=1, file=_StdIn, as_list=True)` <br>
Returns tokens from the input stream specified by `file`.
`_StdIn` is an alias for standard input. 
    
    *Parameters:* <a name="read-params"></a>
    - `*types: callable` <br>
    For each type
    given in `types`, a token is returned converted to the
    specified type, in the given order.
    
    - `amount: int` <br>
    Its effect is to repeat the sequence of `types` by the
    specified amount. That is, `read(*types, amount=n)` is
    equivalent to `read(*(types*n))`, where `types` is a tuple
    of types and `n` is an integer&mdash;but the former is
    more efficient.
    
    - `file` <br>
    A file object or other iterable input stream object
    (e.g. `io.StringIO`) that specifies where to read input from.
    
    - `as_list: bool` <br>
    If `True`, if more than one token is requested, converted
    tokens are returned as a list, and thus input is
    immediately consumed. Otherwise, a generator is
    returned (and no input is consumed).

- *(function)* `jutge.read_while(*types, amount=1, file=_StdIn)` <br>
Returns a generator that yields tokens from the input stream
as long as there are more tokens to be read of the requested type.
Each `next` call to this generator yields the result of
`read(*types, amount=amount, file=file, as_list=True)`.
`_StdIn` is an alias for standard input. 
    
    *Parameters:* refer to the documentation for 
    [`read`'s parameters](#read-params)
    
- *(function)* `jutge.get_line(*, file=_StdIn)` <br>
Returns tokens from the input stream specified by `file`.
`_StdIn` is an alias for standard input. 
    
    *Parameters:*
    - `file` <br>
    A file object or other iterable input stream object
    (e.g. `io.StringIO`) that specifies where to read input from.
    
- *(function)* `jutge.set_eof_handling(mode)` <a name="set-handling"></a>
Sets the global end of input handling mode to `mode` (a member
of the [`jutge.EOFModes`](#EOFModes) enum). 
See [_EOF handling modes_](EOF handling modes) for more information.

    _Parameters:_
    
    - `mode: jutge.EOFModes` <br>
    Handling mode to set.

- *(enum.Enum)* `jutge.EOFModes` <a name="EOFModes"></a>
Enumeration class with the different EOF handling modes. 
See [_EOF handling modes_](EOF handling modes) for more information.
    
    *Members:*
    
    - `RaiseException` <br>
    When active, this handling mode enables the raising of an
    `EOFError` exception when end of input is reached. 
    
    - `ReturnNone` <br>
    When active (default), this handling mode makes functions like
    `read` return `None` as tokens when the end of input
    is reached.



## Extra features

### EOF handling modes

The behaviour of the package's functions when encountering EOF 
(the end of input) can be customized with [`set_eof_handling`](#set-handling), by
passing one of the members of the [`EOFModes` enum](#EOFModes).
Currently, the enum holds two options:
- `ReturnNone`
- `RaiseException`

When `ReturnNone` is set, a `None` object is returned for each token that
is requested after end-of-input. When `RaiseException` is set, an
`EOFError` exception is raised instead.

The first mode may seem more simple because it does not involve any
exceptions. But the second mode is actually much easier to debug, since
if you read more than you thought you would have to read 
(i.e., beyond the end of the input),
that probably means something is wrong with your program,
and thus halting the program immediately and showing a traceback
is much more beneficial than gobbling up the error in silence
and potentially passing on the error to some other unrelated
part of your code.

As a side matter, `read_while` always functions in `RaiseException` mode,
since it needs to catch the error to shut down properly. There is a way
to avoid doing this, but it involves checking for `None` objects in the output 
tokens, which is much more cumbersome.

For backwards compatibility reasons, `ReturnNone` is the default.

----

**Example** <br>
Changing the EOF mode to `RaiseException`:

```python
from jutge import *

set_eof_handling(EOFModes.RaiseException)
```

---

### Recursion limit

When importing the `jutge` package, the maximum depth of the
Python interpreter stack is increased (using
`sys.setrecursionlimit(1000000)`). This feature helps solving some recursive
problems in [Jutge.org](https://jutge.org). 


## Version

The variable `jutge.version` contains the version of the package.

# Credits

- Jordi Petit https://github.com/jordi-petit 
- Albert Lobo https://github.com/llop
- Paolo Lammens https://github.com/plammens


# License

[Apache License 2.0](https://raw.githubusercontent.com/jutge-org/jutge-python/master/LICENSE.txt)
