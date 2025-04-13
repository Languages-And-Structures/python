# print("hello world")
# # to print a large line we can use print like print('''  ''')
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("aman randi hai")
# engine.runAndWait()

# x = 5
# name = "John"
# print(name)
# x = 5
# x = "Sara"
# print(x)
# dynamical typing in python therefore its allowd to redeclare a varaible with different types of words or characters
# a, b, c = 5, 3.2, "Hello"
# print(a)
# print(b)
# print(c)

# first_name = "John"
# last_name = "Doe"
# print(first_name + " " + last_name) 
# Using the + operator between different types (e.g., a string and an integer) without explicit conversion will result in a TypeError.

# global keyword-we can change the value variable inside any function by using it 
# ex:x = 10

# def change_global_x():
#     global x  # Declare x as global
#     x = 20    # Modify the global variable

# print("Before changing:", x)
# change_global_x()
# print("After changing:", x)

# boolean
# Booleans represent one of two values: True or False.
# is_valid = True
# print(is_valid)  # Output: True

# Lists are sequences of elements that maintain an order and can contain items of various types.
# colors = ["red", "green", "blue"]
# print(colors)  # Output: ['red', 'green', 'blue']

# Tuples resemble lists in many aspects, yet they are immutable, signifying that once created, they cannot be altered.
# coordinates = (10.0, 20.0)
# print(coordinates)  # Output: (10.0, 20.0)

# Dictionaries hold key-value pairs. Keys must be unique and immutable.

# person = {"name": "Alice", "age": 25}
# print(person)  # Output: {'name': 'Alice', 'age': 25}

# Sets are unordered collections of unique elements.

# unique_numbers = {1, 2, 3, 3}
# print(unique_numbers)  # Output: {1, 2, 3}

# delete keyword
# no_of_chocolates=10
# del no_of_chocolates
# print(no_of_chocolates)

# type of class
# message="Welcome to India"
# print(message)
# print(type(message))
# output:Welcome to India
# <class 'str'>

# literals
# integer literal
# #positive whole numbers
# x = 2586
# #negative whole numbers
# y = -9856
# # binary literal
# a = 0b10101
# # decimal literal
# b = 505
# # octal literal
# c = 0o350
# # hexadecimal literal
# d = 0x12b
# print (x,y)
# print(a, b, c, d)

# Mantissa-The digits before the symbol E in an exponential literal is known as the mantissa. In computing, it denotes the significant digits of the floating-point numbers.
# Exponent- The digits after the symbol E in an exponential literal are the exponent. It denotes where the decimal point should be placed.
# print(2.537E5)

# Output

# 253700.0

# complex literal
# a=7 + 8j
# b=5j
# print(a)
# print(b)

# The output of the code snippet will be-

# (7+8j)
# 5j

#boolean literals
# x = (1 == 1)  
# y = (7 == False) 
# print("x is", x)  
# print("y is", y)

# The expected output is-

# x is True
# y is False
# tuple literals
# even_numbers = (2, 4, 6, 'mohit')
# vowels=('a','e','i','o','u')  
# print(even_numbers)
# print(vowels)

# identity operators
# number1 = 5
# number2 = 5
# number3 = 10
# print(number1 is number2)  # check if number1 is equal to number2
# print(number1 is not number3)  # check if number1 is not equal to number3

# Output:

# True
# not in ,in are membership operators

# bitwise operator // to see
# number1 = 4  # 0100 in binary
# number2 = 3  # 0011 in binary
# print("& operation- ", number1 & number2)  # AND
# print("| operation- ", number1 | number2)  # OR
# print("^ operation- ", number1 ^ number2)  # XOR
# print("~ operation- ", ~number2)  # negation
# print("<< operation- ", number1 << 1)  # shift left by 1 bit
# print(">> operation- ", number1 >> 1)  # shift right by 1bit

# Output:

# & operation-  0
# | operation-  7
# ^ operation-  7
# ~ operation-  -4
# << operation-  8
# >> operation-  2

# # Here, we take input from the user and then display it.
# name = input("Enter your first name: ")
# print("Hey! " + name)

# Output:

# Enter your first name: Prajit
# Hey! Prajit

# Here, we will take an integer as input from the user.
# age = int(input("Enter your age: "))
# new = age + 1
# name = input("Enter your name: ")
# print("Hey! " + name + " Next year you will be " + str(new))

# Output:

# Enter your age: 19
# Enter your name: Ayush
# Hey! Ayush Next year you will be 20

# List

# # Taking input for a list of strings
# string_list = input("Enter elements separated by space: ").split()
# print("List of strings:", string_list)

# Set

# # Taking input for a set of integers
# integer_set = set(map(int, input("Enter numbers separated by space: ").split()))
# print("Set of integers:", integer_set)

# Tuple

# # Taking input for a tuple of strings
# string_tuple = tuple(input("Enter elements separated by space: ").split())
# print("Tuple of strings:", string_tuple)

# Print with a custom separator
# print("apple", "banana", "cherry", sep=", ")

# Output:

# apple, banana, cherry

# Formatted string literals, commonly known as f-strings, were introduced in Python 3.6. They allow you to embed expressions inside string literals using curly braces {} and a prefix f. Let's take an example:

# name = "Alice"
# age = 25

# # Using f-string for formatting
# formatted_string = f"My name is {name} and I am {age} years old."
# print(formatted_string)

# Output:

# My name is Alice and I am 25 years old.

# str.format
# # Here, we take two variables and do certain operations with them.                                                         
# x = 3
# y = 12
# mul = x * y
# print('The value of x is {} and y is {}'.format(x, y))
# # Here, we are specifying the order of the variables.
# print('{2} is the multiplication of {0} and {1}'.format(x, y, mul))
# # We can even use keyword arguments to format strings.
# print('Hey! Welcome to {company}. In this article we will learn about {language}'.format(company='Scaler', language='Python'))
# a=type(input('mohit'))
# print(a)
# for Loop Syntax
# for val in sequence:
#     loop body