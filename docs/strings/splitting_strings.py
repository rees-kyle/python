# splitting strings
"""
Seperate strings into smaller parts and returns these parts as a list.
"""
# basic syntax
"""
string.split(separator, maxsplit)

'separator' specifies where to split the string.
'maxsplit' specifies the maximum number of splits.
Both arguments are optional.
"""


# splitting by spaces
"""
This is the default.
"""
text = "I am learning Python"
result = text.split()

print(result)

"""
Each word becomes an individual item in  the list.
"""


# Using a custom separator
"""
Specify which character separates the values.
"""
fruits = "apple,banana,cherry"

result = fruits.split(",")

print(result)

"""
The commas are removed during the splitting process.
"""


# limiting the number of splits
"""
The second argument controls how many splits occur.
"""
text = "apple-banana-cherry-orange"

result = text.split("-", 2) # stop splitting after the two first hyphens

print(result)


# accessing split values
"""
Access individual items using indexing.
"""
date = "18/11/2026"

parts = date.split("/")

print(parts[0])
print(parts[1])
print(parts[2])


# practice
colours = "red,green,blue,yellow"

result = colours.split(",")

print(result)
print(result[2])
