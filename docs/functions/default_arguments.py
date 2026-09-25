# default arguments = automatic values when not provided
def greet(name="friend"): # default value is 'friend'
	print("Hello", name)

greet("Kyle")
greet()


# numbers
def multiply(number, by=2):
	return number * by

print(multiply(5)) # uses default value '2'
print(multiply(5, 3)) # overrides default value



# Default arguments must come after normal arguments.
def introduce(name, age=18): # not (age=18, name)
	print(name, age)

# example
def make_coffee(size ="medium", milk=True):
	print("Size:", size)
	print("Milk:", milk)

make_coffee()
make_coffee("large")
make_coffee("small", False)


# practice
def welcome_user(name="guest"):
	print("Welcome", name)

welcome_user("Kyle")
welcome_user()
