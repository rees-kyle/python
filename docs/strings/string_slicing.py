# string slicing = extract part of a string
"""
basic syntax:

text[start:stop]

Python includes the character at 'start', but stops before 'stop'.
"""
text = "Python"

print(text[0:3])
"""
P y t h o n
0 1 2 3 4 5
"""

"""
You can leave out the starting position:
"""
text = "Python"

print(text[:4])
"""
You can also leave out the ending position:
"""
print(text[2:])

"""
Negative indexes count from the end:

 P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
"""
text = "Python"

print(text[-3:])


# third value = step
"""
text[start:stop:step]
"""
text = "Python"

print(text[::2])

"""
Reversing a string:
"""
text = "Python"

print(text[::-1])


# practice
word = "Programming"

print(word[0:4])
print(word[3:7])
print(word[:5])
print(word[5:])
print(word[-4:])
print(word[::2])
print(word[::-1])
