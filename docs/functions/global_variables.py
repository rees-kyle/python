# global variables = outside functions
name = "Alex" # created outside

def greet():
	print(name)

greet()


# usage in multiple functions
score = 10

def show_score():
	print(score)

def double_score():
	print(score * 2)

show_score()
double_score()


# changing a global variable
"""
score = 10

def increase_score():
	score = score + 1 # error: treats it as local

increase_score()
"""
score = 10

def increase_score():
	global score # correct way
	score = score + 1 # shorter version: 'score += 1'

increase_score()

print(score)


# local vs global
message = "Global"

def test():
	message = "Local"
	print(message)

test()
print(message)


"""
Avoid changing global variables unless you have
a good reason. Passing values into functions and 
returning a result is usually cleaner:
"""
def increase_score(score):
	return score + 1

score = 10
score = increase_score(score)

print(score)
