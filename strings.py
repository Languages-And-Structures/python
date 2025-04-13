# Reassigning Strings in Python
# message="Welcome to Scaler"
# print(message)
# message="Hello World" #reassigning a new string
# print(message)

# slicing
# While performing slicing operations, one thing to remember is that the start index value is always included while that of the last index is always excluded.
# Slicing can also be negative or positive, just like indexing in Python!
# message="Welcome to Scaler"
# print(message[2:5]) # positive slicing
# print(message[-10:-2]) #negative slicing
# print(message[:5]) #slicing from the start
# print(message[2:]) #slicing to the end

# Example Program of String Operators in Python
# message1="Hello World!"
# message2="Welcome to Scaler"
# print(message1+message2) # + operator
# print(message1*3) # * operator
# print(message1[6]) # [] operator
# print(message2[0:7]) # [:] operator
# str1="Hello"
# if str1 in message1:# in operator
#     print("It is a present!")
# if str1 not in message2:# not in operator
#     print("It is not present!")

# string slicing using slice operator
# s = "Welcome to scaler docs"
# s1 = slice(6) # takes start as 0 automatically
# print("s1-obj:", s1)
# print("s1-res:", s[s1])
# s2 = slice(2,8) # using slice(start, end, step) without step
# print("s2-obj:", s2)
# print("s2-res:", s[s2])
# s3 = slice(1, 20, 2) # using slice(start, end, step) with step
# print("s3-obj:", s3)
# print("s3-res:", s[s3])

# Output

# s1-obj: slice(None, 6, None)
# s1-res: Welcom
# s2-obj: slice(2, 8, None)
# s2-res: lcome
# s3-obj: slice(1, 20, 2)
# S3-res: ecm osae o

# Note:

# ‘Step’ can never be zero.
# String[ : : ] => start = 0, stop = length of string, step = 1.
# String[2 : : ] => start = 2, stop = length of string, step = 1
# String[ :2: ] => start = 0, stop = 2, step = 1
# String[:6] OR String[1:6] => are valid syntaxes as ‘step’ is an optional parameter for this operation.

# # reversing a string
# s = "welcome to scaler"
# # reversing complete string
# s1 = s[::-1]
# print("s1:", s1)
# # reversing complete string by stepping to every 2nd element
# s2 = s[::-2]
# print("s2:", s2)
# # reversing from 10th index until start, 'stop' index here automatically will be till starting of the string
# s3 = s[10::-1]
# print("s3:", s3)
# # reversing from end until 10th index, 'start' index will automatically be the first element
# s4 = s[:10:-1]
# print("s4:", s4)
# # reversing from 16th index till 10th index
# s5 = s[16:10:-1]
# print("s5:", s5)
# # this will return empty, as we're not reversing here. But NOTE that this 'start' cannot be greater than ‘stop’ until & unless we're reversing
# s6 = s[11:2]
# print("s6:", s6)
# # reversing from 14th index from the end until 4th index from the end.
# s7 = s[-4:-14:-1]
# print("s7:", s7)
# str = "harry"
# count = str.count("harry")
# print(count) 
# we can use find function to use double space

# agr list pe koii function chalaya toh original list hi badal jati hai

# dictionary
# a = {
# "key": "value",
# "harry": "code",
# "marks": "100",
# "list": [1, 2, 9]
# }
# print(a["key"]) # Output: "value"
# print(a["list"]) # Output: [1, 2, 9]

# p=int(input("enter number for which table needs to get printed :"))
# i=1
 
# while(i<11):
#     print(f"{p}*{i}={p*i}")
#     i=i+1

'''
# For n = 3
#   *
#  ***
# *****

# For n = 5
#     *
#    ***
#   *****
#  ********
# **********

# '''

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")iske karan ek new line mil gya
# end=""because of this print statment gives a new line nhi dega by default