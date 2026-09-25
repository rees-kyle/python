# strings

# string = text
name = "Kyle"
message = "Hello, world!"

print(name)
print(message)


# combining
first_name = "Kyle"
last_name = "Rees"

full_name = first_name + " " + last_name
print(full_name)


# f-string = formatted string
name = "Kyle"
age = 25

print(f"My name is {name} and I am {age} tears old.")


# operations
text = "Python Programming"

print(len(text)) # number of characters
print(text.lower()) # lowercase
print(text.upper()) # uppercase
print(text[0]) # first letter
print(text[-1]) # last letter
print(text[0:6]) # first six letters


# combing numbers
age = 25

# incorrect
# print("Age: " + age)

# correct
print("Age: " + str(age))
print(f"Age: {age}")


# example
name = "Kyle"
age = "25"
language = "Python"

print(f"My name is {name}, I am {age} years old, and I am learning {language}.")
