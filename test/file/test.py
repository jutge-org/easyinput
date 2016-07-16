from jutge import read

f = open('lorem-ipsum.txt')
w = read(file=f)
while w is not None:
    print(w)
    w = read(file=f)
