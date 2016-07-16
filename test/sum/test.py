from jutge import read

s = 0
x = read(int)
while x is not None:
    s += x
    x = read(int)
print(s)
