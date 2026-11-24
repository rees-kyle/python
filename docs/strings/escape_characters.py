# escape characters
"""
Special sequences inside strings to represent characters
that would otherwise be difficult to type or display.
"""

# new line
message = "Hello\nWorld"

print(message)

"""
You can use multiple new lines in the same string.
"""
print("Apple\nBanana\nOrange")

"""
Useful for formatting messages, menus or reports.
"""


# tab
print("Name\tAge")
print("James\t25")
print("Sarah\t30")

"""
Useful for organising text into columns.
Not always perfectly aligned as their spacing depends on tab stops.
"""


# quotation marks
message = 'It\'s raining'

print(message)


message = "She said, \"Hello!\""

print(message)


# backslash
text = "Folder\\Documents"

print(text)


# raw strings
"""
Useful for working with regular expressions
or text containing many backslashes.
"""
text = r"Hello\nWorld"

print(text)


# practice
print("Python\nis\tfun!")


message = (
    "Welcome to Python!\n"
    "Today's topic: \"Escape Characters\"\n"
    "Good luck!"
)

print(message)
