# arguments = values given to functions when called

# parameter vs argument
def greet(name): # parameter
	print("Hello", name)

greet("Kyle") # argument

"""
'name' is the parameter.
'Kyle' is the argument.
"""


# example with one argument
def greet(name):
	print(f"Hello, {name}")

greet("Alice")
greet("Bob")


# example with multiple arguments
def add_numbers(a, b):
	total = a + b
	print(total)

add_numbers(5, 3)


# argument order matters
def introduce(name, age):
	print(f"My name is {name} and I am {age} years old.")

introduce("Kyle", 25)


# practice
def favourite_food(food):
	print(f"My favourite food is {food}")

favourite_food("Pizza")
