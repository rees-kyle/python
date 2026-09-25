# looping through collections
"""
Lists, tuples, sets and dictionaries.
"""

# lists
fruits = ["apple", "banana", "cherry"]

for fruit in fruits: # fruit is a temporary variable
	print(fruit)


# tuples
colors = ("red", "green", "blue")

for color in colors:
	print(color)


# sets
numbers = {10, 20, 30}

for number in numbers:
	print(number)


# dictionaries
person = {
	"name": "Kyle",
	"age": 25,
	"city": "London"
}

for key in person: # loop through keys
	print(key)

for value in person.values(): # loop through values
	print(value)


# looping with indexes
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
	print(index, fruit)


# practice
foods = ["pizza", "rice", "pasta"]

for food in foods:
	print("I like", food)


# main idea
"""
for item in collection:
	do something with item
"""
