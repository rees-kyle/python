# recursion = function calls itself to solve a problem
"""
A recursive function needs a base case so it eventually stops.
"""
def countdown(number):
	# base case
	if number == 0:
		print("Done")
		return

	print(number)
	countdown(number - 1) # call same function with smaller number

countdown(5)


# example with return
def factorial(number):
	if number == 1:
		return 1

	return number * factorial(number - 1)

print(factorial(5))


# the two important parts
"""
A recursive function normally has:
"""
def function(value):
	# 1. base case
	if stopping_condition:
		return result

	# 2. recursive case
	return function(smaller_problem)

# for example
def countdown(number):
	if number == 0: # base case
		return

	print(number)
	countdown(number - 1) # recursive case


# recursion vs loops
"""
This:
"""
def countdown(number):
	if number == 0:
		return

	print(number)
	countdown(number - 1)
"""
can also be written with a loop:
"""
for number in range(5, 0, -1):
	print(number)
"""
For many simple problems a loop is easier.
Recursion is useful for trees, nested structures, file systems,
and certain algorithms.
"""
