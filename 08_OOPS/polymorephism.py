'''
Polymorphism: Operator Overloading
When the same operator is allowed to have different meanings according to the context.
'''

# Define a class named Complex to represent complex numbers
class Complex:
    # Constructor to initialize the real and imaginary parts of the complex number
    def __init__(self, real, img):
        self.real = real
        self.img = img 

    # Method to display the complex number
    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    # Overload the addition operator
    def __add__(self, num2):
        newRealNumber = self.real + num2.real 
        newImgNumber = self.img + num2.img
        return Complex(newRealNumber, newImgNumber)
    
    # Overload the subtraction operator
    def __sub__(self, num2):
        newRealNumber = self.real - num2.real 
        newImgNumber = self.img - num2.img
        return Complex(newRealNumber, newImgNumber)
    

num1 = Complex(1, 3) # Create an instance of the Complex class with real part 1 and imaginary part 3
num1.showNumber() # Display the first complex number

num2 = Complex(2, 5) # Create another instance of the Complex class with real part 2 and imaginary part 5
num2.showNumber()

num3 = num1 + num2 # Add the two complex numbers
num3.showNumber() # Display the result of addition

num3 = num1 - num2 # Subtract the second complex number from the first
num3.showNumber() # Display the result of subtraction
