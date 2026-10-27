# Operators

# =,+,-,/ --> these are operators
# Arithmetic Operator - maths calculations
# Comparision Operator - to compare two values
# Assignment Operator - to assign a value to a variable
# Logical operator - to perform logical operations
##

# Arithmetic Operators
# int + int = int
# int + float = float
print(10 + 2.5)
# float + float = float
# int + boolean = int
# float + boolean = float
print(1.0 + True)
# boolean + boolean = boolean
# srt + str = str

# int + str --> TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Multiplication
print(10 * 2.5)
print('Hi ' * 3)

#Division
# no matter what are the data types of the operands, the result of division is always a float.
print(10 / 2)

# Mod operator
# Mod operator returns the remainder of the division of two numbers.
print(10 % 3) # Output: 1
print(7 % 9) # Output: 7

# Floor Division
# Floor division returns the largest integer less than or equal to the result of the division.
print(8/3) # Output: 2.6666666666666665
print(8//3) # Output: 2

# Exponent operator
# Exponent operator returns the result of raising the first operand to the power of the second operand
print(2 ** 3) # Output: 8  
print (9 ** 0.5) # Output: 3.0   

# Comparison Operators
# Comparison operators are used to compare two values.
# ==, !=, <, >, <=, >=
print(10 == 10) # Output: True
print(10 != 10) # Output: False
print(10 < 10) # Output: False
print(10 > 10) # Output: False
print(10 <= 10) # Output: True
print(10 >= 10) # Output: True
print(10 == True)

# Assignment operator
a = 2 + 5
print(a) # Output: 7

# Logical Operators
# Logical operators are used to combine conditional statements.
print(10 > 5 and 10 < 20) # Output: True
print(10 > 5 or 10 < 20) # Output: True

print(10 > 5 and 10 > 20) # Output: False
print(10 > 5 or 10 > 20) # Output: False
print(not(10 > 5 or 10 > 20)) # Output: False

