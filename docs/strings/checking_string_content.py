# checking string content
"""
Methods usually return a Boolean value: True or False.
Useful for validating user input, checking usernames and examining text.
"""

# checking letters and numbers
"""
.isalpha() checks whether a string contains only letters.
"""
text = "Hello"

print(text.isalpha())


"""
.isdigit() checks whether a string contains only digit characters.
"""
number = "12345"

print(number.isdigit())


"""
.isalnum() checks whether a string contains only letters and numbers.
"""
username = "Python123"

print(username.isalnum())

"""
Spaces and punctuation will cause .isalnum() to return False.
"""


# checking spaces and letter case
"""
.isspace() checks whether a string contains only whitespace characters.
"""
text = "   "

print(text.isspace())


"""
.isupper() and .islower() checks whether the letters in a string
are uppercase or lowercase.
"""
text = "HELLO"

print(text.isupper())
print(text.islower())


# checking the beginning and end of strings
"""
.startswith() checks whether a string begins with specified text, while
.endswith() checks whether it finishes with specified text.
"""
filename = "report.txt"

print(filename.startswith("report"))
print(filename.endswith(".txt"))

"""
Useful for checking filename and extensions.
"""


# checking whether text exists
"""
The 'in' keyword checks whether a particular word or character
exists inside a string.
"""
sentence = "I am learning Python"

print("Python" in sentence)
print("Java" in sentence)

"""
You can also use 'not in' to check whether text is absent.
"""
print("Java" not in sentence)

"""
These are case-sensitive, meaning "Python" and "python" are different.
"""


# example
"""
This program checks whether a username contains only letters and numbers.
"""
username = input("Enter username: ")

if username.isalnum():
    print("Valid username")
else:
    print("invalid username")


# practice
password = input("Enter password:")

if password.isalnum() and len(password) >= 8:
    print("Valid password")
else:
    print("Invalid password")

"""
Password must contain only letters and numbers
and must be atleast 8 characters long.
"""
