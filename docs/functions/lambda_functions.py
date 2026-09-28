# lambda functions = short, one-line
# normal function:
def double(number):
	return number * 2

# lambda function:
double = lambda number: number * 2
print(double(5))


# basic structure
"""
lambda input: output
"""

# example
square = lambda x: x * x # take 'x' and return 'x*x'

print(square(4))


# lambda with 2 inputs
add = lambda a, b: a + b

print(add(3, 7))


# when lambda is useful
"""
For small tasks, especially with sorting.
"""
students = [
	{"name": "Ali", "age": 20},
	{"name": "Sare", "age": 18},
	{"name": "Tom", "age": 22}
]

students.sort(key=lambda student: student["age"])

print(students)


# lambda vs normal function
"""
Use a normal function when the code is longer or needs a clear name:
"""
def calculate_total(price, tax):
	return price + tax

"""
Use lambda for quick, simple one-line functions:
"""
calculate_total = lambda price, tax: price + tax


# practice
triple = lambda number: number * 3

print(triple(6))
