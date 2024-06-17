'''
Function is block of statements that perform a specific task. 

Types of functions:
    1) Built-in functions:
        Examples: print(), len(), type(), etc.
    2) User-defined functions:
        Functions created by the user.
'''

# Function definition
def CalculateSum(a, b): # Parameters 
    return a + b # Return the sum of two numbers

sum = CalculateSum(10, 20)  # Call the function with arguments
print(sum)

'''
Print 5 time hello using function
'''

# Function definition
def hello(): # Function without parameters
    print("Hello") # printing a hello

# Call the function 5 times
hello() # Call the function without arguments
hello()
hello()
hello()
hello()


'''
Calculates the average of three numbers.
'''

# Function to find the average of 3 numbers
def avgOfNumber(num1, num2, num3):
    avg = (num1 + num2 + num3)/3 # Calculate the average
    return avg # Return the calculated average


# Call the function with three numbers and store the result
output = avgOfNumber(10, 20, 30)

print(output)



'''
Default parameters
Assigning a default value to parameter, which is used when no argument is passed 
'''


# Function with default parameters that calculates multiplication
def Calcmulti(a = 2, b = 3):
    mul = a * b
    return mul

output = Calcmulti() # function call; return the value
print(output)


# Function with one required parameter and one default parameter that calculates subtraction
def Calcsub(a, b = 3):
    sub = a - b
    return sub

output = Calcsub(5)
print(output)

