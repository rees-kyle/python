# inputs and outputs

# print() = display
print("Hello, world!")
print(42)


# print multiple values
name = "Kyle"
age = 30

print("Name :", name) # string and variable
print("Age :", age)


# f-string
print(
	f"My name is {name} and I am {age} years old."
)


# input() = return string
name = input("Enter your name: ")
print(f"Hello, {name}!")

# return number
# incorrect
age = input("Enter your age: ")
print(type(age)) # return strings unless converted

# correct
age = int(input("Enter your age: "))
print(f"Next year, you will be {age + 1}.")

# return decimal
price = float(input("Enter the price: "))
print(f"The price is £{price:.2f}")


# example
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello, {name}.")
print(f"Next year, you will be {age + 1}")


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

sum = first_number + second_number

print(f"The sum is {sum}.")
