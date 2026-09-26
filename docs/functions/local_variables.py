# local variables = only exists inside its function
def greet():
	message = "Hello" # 'message' is local variable
	print(message) 

greet()

"""
Using a local variable outside the function
will cause an error.

Variables outside a function are global variables.
"""
