# Simple print command in python
print("Hello, World!")
print("5*10")

# multiplication
print(5*10)

# addition
print(5+10)

# subtraction
print(10-5)
print(5-10)

# division
print(10/5)
print(5/10)

# string concatenation
print("Hello" + "World!")
print("Hello" + " " +"World")
print("Hello" + " " + "World" + "!")

city = "Delhi"
country = "India"
print(city + " is in " + country)

print(  """
This
    is a comment
    
    yes it is a comment
    """)

print(type(city))
print(type(5+2))
print(type(5/2))
print(type(True))

# VARIABLES
# 1. variablename must start with a letter or underscore, cannot start with a number
# variable name '1ahn' is invalid
# 2.It cannot have special characters like !, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, / etc.
# 3. It cannot be a reserved keyword in python like 'if', 'else', 'while', 'for', 'def', 'class', etc.
# 4. It cannot have spaces in between, but can use underscores to separate words like 'my_variable_name'.
# 5. It is case sensitive, so 'myVariable' and 'myvariable' are different variables.

# Typecasting
# Typecasting is the process of converting one data type to another data type. 
# In Python, there are several built-in functions that can be used for typecasting. 
# Some of the commonly used typecasting functions are:
# int() - converts a value to an integer
# float() - converts a value to a floating-point number
# str() - converts a value to a string
# bool() - converts a value to a boolean
# #

a = "2"
b = int(a)
print(b)

# input() function
# The input() function is used to take input from the user.
name = input("Enter your name: ")
print("Hello, " + name + "!")
print("input over")

#sep and end parameters in print function
# The sep parameter is used to specify the separator between the values.
print("Hello", "World", sep=" ")
print("Hello", "World", sep="----------")

# The end parameter is used to specify what to print at the end of the line.
print("Hello", "World", end="!n")
print("val")