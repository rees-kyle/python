# comments = notes

# single-line
# this is a comment
print("Hello, world!") # this is also a comment


# multi-line
# this program asks for a name
# and prints a greeting
# to the user
name = input("Enter your name: ")
print(f"Hello, {name}!")

"""
This is a multi-line string.
It is not technically a comment.
Mainly used for docstrings, they describe what a
module, function, class or method does.
"""


# good comment
answer = input("Enter your answer: ")
""" 
convert to lowercase
so the comparison is case-insensitive.
"""
answer = answer.lower()

print(answer)


# bad comment
# set score to zero
score = 0


# example
name = input("Enter your name: ")
year = int(input("Enter birth year: "))
age = 2026 - year
# print user's name and age from input
print(
	f"{name}, you are approximately {age} years old."
)
