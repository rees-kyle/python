# assignment operators

# basic: =
age = 25
name = "Alex"


# add and assign: +=
score = 10
score += 5

print(score) # 15

# alternative
score = score + 5
print(score)


# subtract and assign: -=
balance = 100
balance -= 20

print(balance) # 80


# multiply and assign: *=
number = 4
number *= 3

print(number) # 12


# divide and assign: /=
price = 50
price /= 2

print(price) # 25.0


# floor-divide and assign: //=
number = 17
number //= 5

print(number) # 3


# modulus and assign: %=
number = 17
number %= 5

print(number) # 2


# exponent and assign: **= 
number = 3
number **= 2

print(number) # 9


# strings
message = "Hello"
message += " world"

print(message) # Hello world


# lists
numbers = [1, 2]
numbers += [3, 4]

print(numbers) # [1, 2, 3, 4]


# multiple
x, y, z = 10, 20, 30


# multiple, same value
a = b = c = 0


# example
points = 10
points += 5
points *= 2
points -= 4

print(points) # 26
