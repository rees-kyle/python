# keyword arguments = pass valuesusing parameter name

# the key idea:
"""
function_name(parameter=value)
"""

def greet(name, age):
	print(f"My name is {name}")
	print(f"I am {age} years old")

greet(name="Kyle", age=25) # keyword arguments

"""
With normal positional arguments, order matters.
But with keyword arguments, order does not matter.
Python knows which value belongs to which parameter
because you used the names.
"""


# example
def order_food(item, quantity):
	print(f"You ordered {quantity} {item}")

order_food(item="pizzas", quantity=2)


# mixing positional and keyword arguments
def introduce(name, city):
	print(f"{name} lives in {city}")

introduce("Kyle", city="London")

"""
Positional arguments must come before
the keyword arguments.
"""


# practice
def make_profile(username, level):
	print(f"Username: {username}")
	print(f"Level: {level}")

make_profile(username="python_student", level=1)
