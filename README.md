Simple functions to read input from Python for problems in Jutge.org.

This package exports a `read` function that returns the next token of the
input. The type of the token must be given as a parameter: `read(int)`,
`read(float)`, `read(str)`... In the event no more tokens are available,
`read` returns `None`.

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
