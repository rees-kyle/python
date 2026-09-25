# variables
# variable = named place, stores a value
name = "Kyle" # string
age = 25 # number
height = 1.75 # decimal
is_learning = True # boolean


# '=' to create
score = 100


# usage
name = "Kyle"

print(name)
print("Hello", name)


# changing
score = 10
print(score)

score = 20
print(score)


# calulations
price = 10
quantity = 3
total = price * quantity

print(total)


# naming rules:
# case-sensitive
# letters, numbers, underscores
# no spaces
# no number start
# no Python keywords

# valid
first_name = "Kyle"
age2 = 30
total_price = 50

# invalid
# 2age = 30
# first name = "Kyle"
# class = "Python"

# descriptive
user_age = 25
total_price = 100

# unclear
x = 25
tp = 100


# assigning multiple
name, age, country = "Kyle", 30, "United Kingdom"

print(name)
print(age)
print(country)

# can have same value
a = b = c = 0

print(b)
