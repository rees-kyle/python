# dictionary comprehensions = shorter way to create a dictionary

# dictionary = stores data as key-value pairs
person = {
	"name": "Alex",
	"age": 25
}


# dictionary comprehension
numbers = [1, 2, 3, 4, 5]

squares = {num: num * num for num in numbers}

print(squares)

"""
This means:
new_dictionary = {key: value for item in collection}
"""


# without dictionary comprehension
numbers = [1, 2, 3, 4, 5]

squares = {}

for num in numbers:
	squares[num] = num * num

print(squares)


# using if
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {num: num * num for num in numbers if num % 2 ==0}

print(even_squares)


# strings
words = ["apple", "banana", "cherry"]

word_lengths = {word: len(word) for word in words}

print(word_lengths)


# practice 
numbers = [1, 2, 3, 4]

doubles = {num: num * 2 for num in numbers}

print(doubles)
