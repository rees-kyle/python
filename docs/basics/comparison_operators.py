# comparison operators = compare and return boolean

# operators
age = 18

print(age == 18) # equal to
print(age != 18) # not equal to
print(age > 16) # greater than
print(age < 21) # less than
print(age >= 18) # greater than or equal to
print(age <= 17) # less than or equal to


# equals vs equal to
score = 100 # = assigns a value
print(score == 100) # compares a value


# strings
name = "Alice"

print(name == "Alice")
print(name != "Bob")

# case-sensitive
print("python" == "Python") # false


# if
temperature = 25

if temperature > 20:
	print("It is warm.")


# chained
age = 20
print(18 <= age <= 30)
# alternative
print(age >= 18 and age <= 30)


# example
print(10 == 10) # true
print(10 != 5) # true
print(7 > 12) # false
print(4 < 9) # true
print(6 >= 6) # true
print(3 <= 1) # false
print("Ubuntu" == "ubuntu") # false
