# removing values

# lists
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")	# removes by value
print(fruits)


fruits = ["apple", "banana", "cherry"]

fruits.pop(1) # removes by index
print(fruits)


# dictionaries
student = {"name": "Ali", "age": 20, "grade": "A"}

del student["age"]
print(student)


student.pop("grade")
print(student)


# sets
numbers = {1, 2, 3, 4}

numbers.remove(3)
print(numbers)
