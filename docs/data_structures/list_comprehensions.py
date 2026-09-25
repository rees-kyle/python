# list comprehensions = create new list from existing collection
"""
Basic structure:

new_list = [expression for item in collection]

"""

# normal way
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
	squares.append(number * number)

print(squares)


# list comprehension way
numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)


# using range()
numbers = [number for number in range(1, 6)]

print(numbers)


# adding a condition = to filter values
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# strings
names = ["alice", "bob", "charlie"]

capitalized_names = [name.capitalize() for name in names]

print(capitalized_names)


"""
Remember:

[what_you_want for item in collection]

With a condition:

[what_you_want for item in collection if condition]

"""


# practice
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_greater_than_five = [number for number in numbers if number > 5]

print(numbers_greater_than_five)
