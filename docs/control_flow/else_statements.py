# else statements = for false conditions
# does not check a new condition unlike 'elif' statements

# structure
"""
if condition:
	# runs if conidition is true
else:
	# runs if conidition is false
"""


# examples
age = 16

if age >= 18:
	print("You are an adult.")
else:
	print("You are not an adult.")


password = "python123"

if password == "admin123":
	print("Access granted")
else:
	print("Access denied")
