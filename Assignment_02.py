# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

# Task_01 Solution :

i = int(input("Enter a number: "))

if i%2==0:
    print(i,"is an even number")
else:
    print(i, "is an odd number")

# Task2: Sum of Integers from 1 to 50 Using a Loop
# Problem Statement: Write a Python program that:
# 1.Uses a for loop to iterate over numbers from 1 to 50.
# 2.Calculates the sum of all integers in this range.
# 3.Displays the final sum.

# Task_02 Solution :

IntegerSum = 0
n = range(0,51)
for x in n:
    IntegerSum+=x
print("The sum of numbers from 1 to 50 is: ",IntegerSum)




