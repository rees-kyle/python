# searching text
# using 'in'
"""
Checks whether text exists.
"""
text = "Hello Python"

print("Python" in text) # True

print("Java" in text) # False


# using 'find()'
"""
Returns the string index of text.
"""
text = "Hello Python"

print(text.find("Python")) # 6

print(text.find("Java")) # -1, not found (python indexes start at 0)


# using 'index()'
"""
Works like 'find()', but raises a 'ValueError' if text is not found.
"""
text = "Hello Python"

print(text.index("Python")) # 6


# using 'count()'
"""
Counts how many times text appears.
"""
text = "apple banana apple"

print(text.count("apple")) # 2


# using 'startswith()' and 'endswith()'
"""
Checks whether a string begins or ends with specific text.
"""
text = "Hello Python"

print(text.startswith("Hello")) # True

print(text.endswith("Python")) # True


# case sensitivity
"""
String searches are case-sensitive.
Use '.lower()' to ignore uppercase and lowercase differences.
"""
text = "Hello Python"

print("python" in text) # False

print("python" in text.lower()) # True
