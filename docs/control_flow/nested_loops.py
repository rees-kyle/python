# nested loops = a loop inside another loop
"""
Useful for working with tables, grids, patterns, lists, matrices etc

Structure:
Inner loop = repeats smaller task inside it
Outer loop = repeats big task
"""
for row in range(3): # outer loop
	for column in range(4): # inner loop runs after outer loop
		print(row, column)


# examples
for i in range(4):
	for j in range(5):
		print("*", end="")
	print()

for i in range(1,6):
	for j in range(i):
		print("*", end="")
	print()

numbers = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

for row in numbers:
	for number in row:
		print(number)
