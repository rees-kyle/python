# removing spaces
# strip()
"""
Remove spaces from both ends.
"""
name = "   Pyhton   "

clean_name = name.strip()

print(clean_name)


# lstrip()
"""
Remove spaces from the beginning.
"""
name = "   Python   "

clean_name = name.lstrip()

print(f"'{clean_name}'")


# rstrip()
"""
Remove spaces from the end.
"""
name = "   Python   "

clean_name = name.rstrip()

print(f"'{clean_name}'")


# replace()
"""
Remove all spaces.
"""
message = "Hello Python World"

clean_message = message.replace(" ", "") # find a space, replace it with nothing

print(clean_message)


# Remove extra spaces between words
"""
Keep one space between words, remove extra.
"""
message = "Hello    Python     World"

clean_message = " ".join(message.split())
"""
'split()' seperates the words.
'" ".join()' joins them together with one space between each word.
"""

print(clean_message)


# important: strings are immutable
"""
String methods do not modify the original string.
They return a new string.
"""
name = "   Python   "

name.strip()

print(f"'{name}'")

"""
To save the change, assign the result:
"""
name = name.strip()
print(f"'{name}'")
