# sorting data = in order

# numbers
numbers = [5, 2, 9, 1, 7]

numbers.sort()

print(numbers)


# strings
fruits = ["banana", "apple", "cherry"]

fruits.sort()

print(fruits)


# reverse order
numbers.sort(reverse=True)

print(numbers)


# sorted() = new list
sorted_numbers = sorted(numbers)

print(sorted_numbers)


# sorting by length
names = ["Sam", "Alexander", "Jo", "Maria"]

names.sort(key=len)

print(names)


# dictionaries
scores = {
	"Alice": 85,
	"Bob": 92,
	"Charlie": 78
}

sorted_scores = sorted(scores.items()) # sort by key

print(sorted_scores)

sorted_scores = sorted(scores.items(), key=lambda item: item[1])

print(sorted_scores)


"""
list.sort() changes the original list.
sorted(list) creates a new sorted list.
"""


# practice
ages = [34, 12, 67, 23, 9]

ages.sort(reverse=True)

print(ages)
