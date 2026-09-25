# data types = values

# integer = number
age = 25
temperature = -4


# float = decimal
price = 19.99
height = 1.75


# string = text
name = "Kyle"
message = "Hello, World!"


# boolean = true or false
is_logged_in = True
has_paid = False


# list = in order
colours = ["red", "green", "blue"]
scores = [10, 20]


# tuple = unchangable
coordinates = [10, 20]


# set = no order
numbers = {1, 2, 3}


# dictionary = key-value pairs
person = {
	"name": "Kyle",
	"age": 25,
}


# none = no value
result = None


# checking = type function
age = 25
print(type(age))


# changing data type
value = 10
print(type(value))

value = "ten"
print(type(value))


# mistakes
# numbers as strings
number_one = 10
number_two = "10" #string

print(type(number_one)) #int
print(type(number_two)) #str

# adding a string and integer
age = "25"
#print(age + 5)
