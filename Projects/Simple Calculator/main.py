'''
Simple Calculator
'''

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract second number from first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide first number by second
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Function to raise first number to the power of second
def power(x, y):
    return x ** y

# Loop to keep the calculator running until the user decides to exit
while True:
    # Print the options for the user
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("Q. Quit")

    # Take input from the user to choose an operation
    choice = input("Enter choice (1/2/3/4/5 or Q to quit): ")

    # Check if the user wants to exit the program
    if choice.upper() == 'Q':
        print("Exiting the calculator. Goodbye!")
        break

    # Take input from the user for the numbers to operate on
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation based on user's choice and print the result
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", power(num1, num2))
    else:
        print("Invalid input")
