from jutge import read

# int
print('enter an int:')
a = read(int)
print('Type name: ' + type(a).__name__)
print('Value: ', end ='')
print(a)

# float
print('enter a float:')
a = read(float)
print('Type name: ' + type(a).__name__)
print('Value: ', end ='')
print(a)

# char
print('enter a character:')
a = read(chr)
print('Type name: ' + type(a).__name__)
print('Value: ', end ='')
print(a)
print('enter three characters:')
a, b, c = read(chr, chr, chr)
print(a, b, c)

# str
print('enter a string:')
a = read()
print('Type name: ' + type(a).__name__)
print('Value: ', end ='')
print(a)
print('enter another string:')
a = read(str)
print('Type name: ' + type(a).__name__)
print('Value: ', end ='')
print(a)

# iter
print('enter a string (read as string iterator):')
a = read(iter)
print('Type name: ' + type(a).__name__)
for c in a: print(c, end = ' ')
print()


# an invented type
class mytype:
  def __init__(self, word): self.word = word
  def sayAWord(self): print(self.word)

print('enter a string (read as mytype):')
a = read(mytype)
print('Type name: ' + type(a).__name__)
a.sayAWord()
