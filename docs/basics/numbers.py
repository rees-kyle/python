# numbers = 3 types

# integers = whole
age = 25
temperature = -3
population = 1000000

print(age)
print(type(age))


# floats = decimal
price = 19.99
height = 1.75
temperature = -2.5

print(price)
print(type(price))


# complex = real and imaginary
number = 3 + 4j

print(number)
print(type(number))


# arithmetic 
a = 10
b = 3

print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # floor division (removes decimal)
print(a % b) # remainder
print(a ** b) # power


# division difference
print(10 / 3) # normal
print(10 // 3) # floor


# conversion
number_text = "25" # text

number = int(number_text)
decimal = float(number_text)

print(number)
print(decimal)

price = 19.99 # decimal
whole_number = int(price)

print(whole_number) # decimal removed, not rounded


# rounding
number = 3.14159

print(round(number))
print(round(number, 2)) # 2 decimal places


# functions
print(abs(-12)) # absolute
print(min(4, 8, 2)) # smallest
print(max(4, 8, 2)) # largest
print(pow(2, 3)) # power


# underscores
population = 1_000_000 # 1000000
salary = 50_000 # 50000

print(population)


# example
price = 15.50
quantity = 4
tax_rate = 0.20

subtotal = price * quantity
tax = subtotal * tax_rate
final_total = subtotal + tax

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Final Total:", final_total)
