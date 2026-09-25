# return values = result of function
def add_numbers():
	return 5 + 3

answer = add_numbers()

print(answer)


# return vs print
"""
'print()' only displays something.
"""
def greet():
	print("Hello")

greet()


"""
'return' gives a value back to be stored or used later.
"""
def get_greeting():
	return "Hello"

message = get_greeting()

print(message)


# example with parameters
def multiply(a, b):
	return a * b # send back the answer

result = multiply(4, 5)

print(result)


# using returned values later
def square(number):
	return number * number

answer = square(6) # function returns '36'

print(answer + 10) # then python adds '10'


# important rule
"""
When Pyhton reaches return, the function stops.
"""
def test():
	return "Done"
	print("This will not run") # ignored after return

print(test())


# practice
def subtract(a, b):
	return a - b

answer = subtract(10, 4)

print(answer)
