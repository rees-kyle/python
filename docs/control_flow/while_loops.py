# while loops = repeats code for true conditions
count = 1

while count <= 5: # run loop while count <= 5
	print(count)
	count += 1


# avoid infinite loops, conditions should eventually become false.
"""
count = 1

while count <=5:
	print(count)
"""


# example
password = ""

while password != "python123": # run loop while password is !=
	password = input("Enter the password: ")

print("Access granted!")
