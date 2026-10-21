# changing letter case
# convert to uppercase
text = "hello world"

print(text.upper())


# convert to lowercase
text = "HELLO WORLD"

print(text.lower())


# capitalise first letter
text = "hELLO WORLD"

print(text.capitalize())


# capitalise each word
text = "hellow world from python"

print(text.title())


# swap uppercase and lowercase
text = "Hello World"

print(text.swapcase())


# advanced lowercase conversion
"""
For more thorough case-insensitive comparisons
across different languages.
"""
text = "Straße"

print(text.lower())
print(text.casefold())


# Strings are immutable
"""
They do not change the original string.
They create a new string.
"""
name = "alice"

name.upper()

print(name)

"""
To keep the change, assign the result back to the variable:
"""
name = "alice"

name = name.upper() # here

print(name)


# example: case-insensitive comparisons
"""
Suppose you ask someone to enter "yes".
"""
answer = input("Do you want to continue?")

if answer.lower() == "yes":
	print("Continuing...")
else:
	print("Stopping...")

"""
This accepts:
yes
YES
Yes
yEs

All of these become "yes" when '.lower()' is applied.

You can also use '.strip()' to remove accidental spaces:
"""

if answer.strip().lower == "yes":
	print("Continuing")


# practice
"""
Convert to uppercase.
"""
message = "python is fun"

print(message.upper())


"""
capitalise the first letter in each word.
"""
city = "new york city"

print(city.title())


"""
Write a program that asks the user for their name
and always displays it in lowercase,
regardless of how they entered it.
"""
name = input("Enter your name: ")

print(name.lower())
