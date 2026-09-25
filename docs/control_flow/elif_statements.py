# elif statements = else if

# structure
"""
if condition_1:
	# runs if condition_1 is true
elif condition_2:
	# runs if condition_1 is false and condition_2 is true
elif condition_3:
	# runs if previous conditions are false and condition_3 is true
else:
	# runs if none of the conditions are true

# only the first true condition runs, the rest is skipped.
"""

# examples
score = 75

if score >= 90:
	print("Grade A")
elif score >= 80:
	print("Grade B")
elif score >= 70:
	print("Grade C")
else:
	print("Grade D or below")


temperature = 18

if temperature > 30:
	print("Hot")
elif temperature > 20:
	print("Warm")
elif temperature > 10:
	print("Cool")
else:
	print("Cold")


age = 16

if age >= 18:
	print("Adult")
elif age >= 13:
	print("Teenager")
else:
	print("Child")
