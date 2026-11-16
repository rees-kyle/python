# replacing text
"""
'.replace()' method allows you to replace words, characters,
or parts of a string with different text.
Useful for correcting text, changing information and cleaning data.
"""

# basic syntax
"""
string.replace(old, new)

for example:
"""
message = "I like apples"

result = message.replace("apples", "bananas") 

print(result)


# replacing multiple occurrences
"""
By default, '.replace()' replaces every occurrence.
"""
text = "cat dog cat bird cat"

result = text.replace("cat", "rabbit")

print(result)

"""
You can also specify how many occurrences to replace
using a third argument:
"""
result = text.replace("cat", "rabbit", 2) # replace first two occurrences

print(result)


# removing characters
"""
Remove unwanted characters by replacing them with an empty string.
Useful for removing punctuation, spaces or unwanted symbols.
"""
text = "Hello!!!"

result = text.replace("!", "")

print(result)


# string are immutable
"""
'.replace()' creates a new string rather than changing the original.
"""
text = "Hello World"
text = text.replace("World", "Python")

print(text)


# case sensitivity
"""
'.replace()' distinguishes uppercase from lowercase letters.
Replacing "python" will not replace "Python".
"""


# practice
sentence = "I love cats. Cats are amazing"

sentence = sentence.replace("cats", "dogs")
sentence = sentence.replace("Cats", "Dogs")

print(sentence)
