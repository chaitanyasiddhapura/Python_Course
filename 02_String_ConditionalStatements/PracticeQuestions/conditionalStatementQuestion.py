'''
Practice Question
'''

# Q1. Write a program to check if a number entered by the user is odd or even

print("Check number is even or odd")
# input 
number = int(input("Enter a number: "))

# Logic
if(number % 2 == 0):
    print("It's even number")
else:
    print("It's odd number")

# Q2. Write a program to find greatest of 3 number entered by the user.

print("Find greatest of 3 number")
# input 
num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
num3 = int(input("Enter a number 3: "))

# Logic
if( num1 >= num2 and num1 >= num3 ):
    print("Greatest number is: ", num1)
elif( num2 >= num3):
    print("Greatest number is: ",num2)
else:
    print("Greatest number is: ", num3)

# Q3. Write a program to check if number is a multiple of 7 or not

print("Check if number is a multiple of 7 or not")
# input 
number = int(input("Enter a number: "))

# logic
if(number % 7 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not a multiple of 7")