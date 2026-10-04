# string indexing
"""
A string is a sequence of characters,
each character having a position called an index.
"""
text = "Python"

"""
P y t h o n
0 1 2 3 4 5
"""

"""
You access a character using a square bracket:
"""
text = "Python"

print(text[0])
print(text[3])

"""
You can also use negative indexes to count backwards from the end:

 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
"""
text = "Python"

print(text[-1])
print(text[-2])

"""
You can use indexes with variables too:
"""
name = "Daniel"

first_letter = name[0]
last_letter = name[-1]

print(first_letter)
print(last_letter)

"""
Strings cannot be changed directly using an index.
This does not work:

word = "cat"
word[0] = "b"

This does work:
"""
word = "cat"
word = "b" + word[1:]

print(word)

# key idea = string[index]
