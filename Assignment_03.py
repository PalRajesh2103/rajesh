# Task 1: Calculate Factorial Using a Function
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

#Using Recursion:

# def factorial_pro(x):                               # function declaration
#     if (x<2):
#         return 1
#     else:
#         fr=x*(factorial_pro(x-1))                   # Factorial calculates
#         return fr
# result=factorial_pro(5)                             # Fn. called
# print(result)

# Using loop :
# def factorialExp(x):
#     result=1
#     for i in range(1,x+1):
#         result*=i
#     return result
#
# num=int(input("Enter a number: "))
# r=factorialExp(num)
# print("Factorial of 5 is: ",r)

#Q.2) Using the Math Module for Calculations
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:Square root of the number,Natural logarithm (log base e) of the number,Sine of the number (in radians)
# 3.   Displays the calculated results.

from math import *
#import math

num = int(input("Enter a number: "))

# print("Square root: ",math.sqrt(num))
# print("Logarithm: ",math.log(num))
# print("Sine: ",math.sin(num))

print("Square root: ",sqrt(num))
print("Logarithm: ",log(num))
print("Sine: ",sin(num))

