# type conversion

# functions:
# int()
age = "25"
age_number = int(age)

print(age_number)
print(type(age_number))

# float()
price = "9.99"
price_number = float(price)

print(price_number)

# str()
score = 100
message = "Your score is " + str(score)

print(message)

# bool()
print(bool(1))			# true
print(bool(0))			# false
print(bool("Hello"))	# true
print(bool(""))			# false


# user input = returns string
age = int(input("Enter your age: "))
next_year = age + 1

print(f"Next year, you will be {next_year}.")


# invalid
"""
number = int("Hello") # error
"""
number = int("50") # correct


# example

name = input("Enter your name: ")
age = int(input("Enter your age: "))

future_age = age + 5

print(
	f"{name}, you will be {future age} years old in five years."
)
