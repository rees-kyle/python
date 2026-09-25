# updating values = changing existing values

# lists
fruits = ["apple", "banana", "cherry"]

fruits[1] = "orange"

print(fruits)


# dictionaries
person = {
	"name": "Alex",
	"age": 25,
	"city": "London"
}

person["age"] = 26 # update a single value

print(person)


person.update({ # update multiple values
	"age": 27,
	"city": "Manchester"

})

print(person)


# sets
numbers = {1, 2, 3}

numbers.remove(2) # numbers.discard is safer
numbers.add(20)

print(numbers)


# tuples = can not be updated
