# booleans = true or false

# creating
is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)


# comparisons
print(10 > 5) # greater than
print(10 <= 5) # less than or equal to
print(10 == 10) # equal to
print(10 != 10) # not equal to


# if
is_raining = True

if is_raining:
	print("Take an umbrella")
else:
	print("No umbrella needed.")


# operators
age = 25
has_ticket = True

print(age >= 18 and has_ticket)
print(age < 18 or has_ticket)
print(not has_ticket) # reverse


# conversions
print(bool(1)) # true
print(bool(0)) # false
print(bool("Python")) # true
print(bool("")) # false
print(bool([1, 2])) # true
print(bool([])) # false


# example
temperature = 18
is_sunny = True

print("Example:")
print(temperature > 20)
print(is_sunny and temperature > 15)
print(not is_sunny)
