'''
The 'match' statement in Python, introduced in Python 3.10, is similar to a switch-case statement found in other programming languages. 
It allows you to compare a value against different patterns (cases) and execute specific code depending on which pattern matches.
'''

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

operation = input("Enter a operation: ")

match(operation):
    case '+':
        print(num1,"+",num2,"=",num1 + num2)
    case '-':
        print(num1,"-",num2,"=",num1 - num2)
    case '*':
        print(num1,"*",num2,"=",num1 * num2) 
    case '/':
        print(num1,"/",num2,"=",num1 / num2) 
    case '%':
        print(num1,"%",num2,"=",num1 % num2)
    case _:
        print("Wrong case...")

