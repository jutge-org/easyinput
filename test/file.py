from jutge import read

f = open('/etc/passwd')
w = read(file=f)
while w is not None:
    print(w)
    w = read(file=f)
