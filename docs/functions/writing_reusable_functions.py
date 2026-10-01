# writing reusable functions
# avoid hard-coded values:
def greet():
	print("Hello, Sam")

greet()

"""
This is reusable:
"""
def greet(name): # parameter 'name' makes function reusable
	print(f"Hello, {name}")

greet("Sam")
greet("Alex")
greet("Maya")


# return results when possible
"""
Instead of:
"""
def add(a, b):
	print(a + b)

"""
You can write:
"""
def add(a, b):
	return a + b # return usually makes a function more flexible
"""
Then reuse the result:
"""
total = add(5, 3)

print(total)
print(total * 2)


# give functions one clear job
"""
A good reusable function should normally do one specific task.
"""
def calculate_area(width, height):
	return width * height
"""
Then:
"""
room1 = calculate_area(5, 4)
room2 = calculate_area(10, 3)

print(room1)
print(room2)


# use clear names
"""
This works:
"""
def x(a, b):
	return a * b

"""
But this is easier to understand:
"""
def calculate_price(quantity, price):
	return quantity * price


# use default arguments when useful
def greet(name, greeting="Hello"):
	print(f"{greeting}, {name}")
"""
You can use the default:
"""
greet("Sam")

"""
Or provide another value:
"""
greet("Sam", "Welcome")


# example of a reusable function
def calculate_discount(price, discount_percent):
	discount = price * discount_percent / 100
	return price - discount

"""
You can reuse for many prices:
"""
print(calculate_discount(100, 20))
print(calculate_discount(50, 10))
print(calculate_discount(200, 25))


# the main idea:
"""
Write a function once, give it different inputs,
and reuse it wherever you need it.
"""
