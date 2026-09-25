# parameters = send information into function

# examples
def greet(name): # name = parameter
	print("Hello", name)

greet("Kyle")


def add_numbers(a, b):
	print(a + b)

add_numbers(5, 3)


# multiple parameters
def introduce(name, age):
	print("My name is", name)
	print("I am", age, "years old")

introduce("Kyle", 25)


# error
"""
def greet(name):
	print("Hello", name)

greet() # expects one value
"""


# practice
def favourite_food(food):
	print("My favourite food is", food)

favourite_food("pizza")
