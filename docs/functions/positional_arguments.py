# positional argument
"""
An argument matched to a parameter
based on position.
"""

def greet(name, age):
	print(f"My name is {name}")
	print(f"I am {age} years old")

greet("Kyle", 25) # order matters
greet(25, "Kyle") # incorrect order


# another example
def subtract(a, b):
	return a - b

print(subtract(10, 3))
print(subtract(3, 10)) # gives a different result


# positional arguments vs keyword arguments
# positional:
def introduce(name, city):
	print(f"{name} lives in {city}")

introduce("Kyle","London")

# keyword:
introduce(city="London", name="Kyle")
"""
Order does not matter.
"""


# practice
def divide(a, b):
	return a / b

answer = divide(20, 4)

print(answer)
