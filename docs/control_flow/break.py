# break = stop loop even if condition True
"""
Commonly used when you find what you are looking
for and no longer need the loop to continue.
"""
for number in range(1, 10):
	if number == 5:
		break
	print(number)
