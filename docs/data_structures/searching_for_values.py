# searching for values

# lists
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) # in


fruits = ["apple", "banana", "cherry"] 

if "banana" in fruits:
	print("Banana is in the list") # or if statement
else:
	print("Banana is not in the list")


# index
fruits = ["apple", "banana", "cherry"]

position = fruits.index("banana")

print(position)


# dictionaries
person = {
	"name": "Kyle",
	"age": 25,
	"city": "London"
}

print("age" in person) # search for a key
print("London" in person.values()) # serch for a value


# sets
numbers = {10, 20, 30}

print(20 in numbers)


# practice
foods = ["pizza", "pasta", "rice"]

if "pasta" in foods: # value in collection
	print("Found it")
else:
	print("Not found")
