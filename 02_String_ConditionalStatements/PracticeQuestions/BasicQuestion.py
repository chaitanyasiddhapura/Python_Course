'''
Q1. Write program to input 2 number & print  sum
'''

print("\"Calculate a Sum\"")

# input 
number1 = int(input("Enter a Number1:"))
number2 = int(input("Enter a Number2: "))

# Logic 
sum = number1 + number2

# Output 
print("Addition is: ", sum)


'''
Q2. Write program to input side of square & print its area 
'''

print("\"Calculate a area of square\"")
# input
SideofSquare = float(input("Enter a side of square: "))

# Logic 
areaOfSquare =  SideofSquare * SideofSquare

# output 
print("Area of square is: ",areaOfSquare)


'''
Q3. Write program to input 2 floating point number & print their average

'''
print("\"Calculate a average\"")
# input 
number1 = float(input("Enter a Number1: "))
number2 = float(input("Enter a Number2: "))

# Logic 
average = (number1 + number2) / 2

# Output
print("Average is: ", average)


'''
Q4. Write program to input 2 number A and B, print true both are eqal to or greater then if not print false 
'''
print("\"Find greater then or eqal to number\" ")
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))

if(a >= b):
    print("A is greater than or equal to B")
else:
    print("B is greater than A")

