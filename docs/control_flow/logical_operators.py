# logical operators = combine conditions
"""
Used in if statements and loops:
and
or
not
"""


# and
age = 20
has_id = True

if age >= 18 and has_id: 		# both conditions must be true
	print("You can enter")


# or
is_student = True
is_senior = False

if is_student or is_senior:		# one condition must be true
	print("You get a discount")


# not = reverse
is_raining = False

if not is_raining:				# flips true/false
	print("Go outside")
