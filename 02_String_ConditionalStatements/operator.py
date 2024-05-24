'''
Arithmetic operator (+, -, *, /, %, **) 
'''

#input 
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# Logic 
sum = num1 + num2 
sub = num1 - num2 
mul = num1 * num2 
div = num1 / num2
rem = num1 % num2 
power = num1 ** num2 

# Print Output 
print("Sum: ", sum)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", div)
print("Remainder: ", rem)
print("Power: ", power)

'''
 Relation / Comparison operator (==, <, <=, >, >=, !=)
'''

# Logic  
print(num1 == num2) 
print(num1 < num2)
print(num1 <= num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 != num2)


'''
Assignment operators (+=, -=, *=, /=, %=, **=)
'''

num3, num4, num5, num6, num7, num8 = 10 , 20, 30 , 40, 50, 60

# Logic
num3 += 10
print(num3)

num4 -= 10 
print(num4)

num5 *= 10
print(num5)

num6 /= 10
print(num6)

num7 %= 10
print(num7)

num8 **= 10
print(num8)

'''
Logical operators (not, and, or)
'''

# Logic 
print(not True)
print(True and True)
print(False or True)
