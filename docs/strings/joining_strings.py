# joining strings
"""
.join() method combines multiple strings into a single string
using a specified separator. Useful when working with lists of words.
"""

# basic syntax
"""
separator.join(iterable)

The separator determines what goes between each string.
"""
words = ["I", "love", "Python"]

sentence = " ".join(words) # " " places spaces between each word

print(sentence)


# using different separators
"""
You can use any string as a separator.
"""
words = ["apple", "banana", "orange"]

print(",".join(words))
print("-".join(words))
print("/".join(words))
print("".join(words)) # empty string


# joining numbers
"""
.join() only accepts strings. Integers must be converted before joining.
"""
numbers = [10, 20, 30]

result = ", ".join(str(n) for n in numbers)

print(result)


# splitting and joining strings
date = "19-11-2026"

parts = date.split("-")

result = "/".join(parts)

print(result)


# practice
words = ["Python", "is", "easy", "to", "learn"]

sentence = "-".join(words)

print(sentence)
