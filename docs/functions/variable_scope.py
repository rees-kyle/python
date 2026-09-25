# variable scope = where a variable can be used

# local variables = variables created inside a function
def greet():
	name = "Kyle"
	print(name)

greet()

# error = 'name' cannot be used outside the function
"""
def greet():
	name = "Kyle"

greet()

print(name)
"""


# global variables = variable created outside function
name = "Kyle"

def greet():
	print(name)

greet()


# local variable with same name as global variable
"""
A local variable can have the same name
as a global variable.
"""
name = "Kyle"

def greet():
	name = "Alex"
	print(name)

greet()
print(name)


# changing a global variable
"""
It is better to avoid changing global variables
inside functions. But Python allows it using 'global'.
"""
count = 0

def increase_count():
	global count
	count = count + 1

increase_count()

print(count)


# better way: use parameters and return
"""
Variables made outside a function can be read
inside a function, but should usually pass values
into functions using parameters.
"""
def increase_count(count):
	return count + 1

count = 0
count = increase_count(count)

print(count)


# practice
score = 10

def add_points(score):
	score = score + 5
	return score

new_score = add_points(score)

print(score) # original score stays the same
print(new_score) # function returns a new value
