# sets = collection of values
"""
Use a set when you need a collection of unique items.
Useful for checking mempership.
"""
fruits = {"apple", "banana", "orange"}

print(fruits)


# adding
fruits.add("mango")

print(fruits)


# removing
fruits.remove("banana")

print(fruits)


# removing duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)


# common set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # union
print(a & b) # intersection
print(a - b) # difference
