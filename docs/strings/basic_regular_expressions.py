# basic regular expressions
"""
A regular expression (regex) is a pattern
used to search, match or replace text.
Useful when you need to find specific types of information,
such as numbers, email addresses, or words within a string.
"""

# importing the 're' module
import re

"""
No install needed as it is included with Python.
"""


# searching for text with 're.search()'
"""
Searches the string for the first occurrence of a pattern:
"""
import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Match found")
else:
    print("No match") 


# Retrieving the matching text using '.group()'
import re

text = "I love Python"

result = re.search("Python", text)

print(result.group())


# common regex patterns
r"""
Regular expressions use special characters
to identify different types of text.

Pattern |   Meaning
------------------------
   \d	|   Matches a digit
   \D	|   Matches a non-digit
   \w	|   Matches a word character
   \s	|   Matches whitespace
   .	|   Matches almost any character
   +	|   One or more repetitions
   *	|   Zero or more repetitions
   ^	|   Beginning of a string
   $	|   End of a string

For example '\d+' matches one or more consecutive digits.
"""


# find all matches
"""
're.findall()' searches for every occurrence and returns a list.
"""
import re

text = "I have 5 apples and 12 oranges"

numbers = re.findall(r"\d+", text)

print(numbers)


# replacing text with 're.sub()'
import re

text = "My phone number is 12345"

result = re.sub(r"\d", "*", text)

print(result)


# splitting strings with 're.split()'
import re

text = "apple,banana;orange"

fruits = re.split(r"[,;]", text) # split string at , or ;

print(fruits)


# example
"""
Extracting numbers from a sentence:
"""
import re

sentence = "John is 25 and Sarah is 30"

ages = re.findall(r"\d+", sentence)

print(ages)

"""
Useful for extracting numerical information
from documents, messages, or data sets.
"""


# practice
"""
Write a program that finds all numbers in this sentence:
"""
import re

text = "I bought 3 apples, 15 bananas and 7 oranges"

results = re.findall(r"\d+", text)

print(results)
