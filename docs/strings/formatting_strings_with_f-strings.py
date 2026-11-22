# formatting strings with f-strings
"""
f-strings allow you to insert variables and calculations directly into text,
they make code easier to read and are useful for displaying information.
"""

# basic syntax
name = "James"
age = "25"

print(f"My name is {name} and I am {age} years old.")

"""
Without f-strings you would have to combine strings manually:
"""
print("My name is " + name + " and I am " + str(age) + " years old.")

"""
f-strings are simpler and easier to maintain.
"""


# calculations inside f-strings
a = 10
b = 5

print(f"Addition: {a + b}")
print(f"Multiplication: {a * b}")

"""
Python evaluates the expressions before inserting the results into the strings.
"""


# formatting decimal numbers
"""
Use ':.2f' to display a number with two decimal places.
"""
price = 19.9876

print(f"Price: £{price:.2f}")

"""
Change the number of decimal places by replacing '2' with another number.
"""


# fromatting percentages and large numbers
"""
Use ':.0%' to display a decimal as a percentage.
"""
discount = 0.15

print(f"Discount: {discount:.0%}")

"""
Use ':,' to add commas to large numbers.
"""
salary = 45000

print(f"Salary: £{salary:,}")

"""
You can combine these formatting techniques when necessary.
"""


# example
product = "Laptop"
price = 799.99
quantity = 3

total = price * quantity

print(f"Product: {product}")
print(f"Price: £{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: £{total:,.2f}")


# practice
customer = "Sarah"
item = "Keyboard"
price = 49.99
quantity = 4

total = price * quantity

print(f"Customer name: {customer}")
print(f"Item name: {item}")
print(f"Item price: £{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: £{total:.2f}")
