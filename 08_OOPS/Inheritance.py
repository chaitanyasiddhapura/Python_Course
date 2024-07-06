'''
When one class(Child/derived/sub class) derives the properties & methods of another class(parent/base/super class) 

Type Of inheritance 
    1. Single Inheritance
    2. Multi Level Inheritance
    3. Multiple Inheritance

'''

'''
Example Of Single Inheritance
'''
# Base class or parent class
class Animal:
    # Method of the base class
    @staticmethod
    def speak():
        print("Animal speaks")

# Derived class or child class that inherits from the Animal class
class Dog(Animal):
    # Method of the derived class
    @staticmethod
    def Name():
        print("Dog")

# Creating an instance of the derived class Dog
dog_instance = Dog()

# Calling the method of the derived class using the instance
dog_instance.Name()

# Calling the method of the base class using the instance of the derived class
dog_instance.speak()

'''
Example Of Multi Level Inheritance
'''

# Base class or parent class
class a:
    # Constructor method to initialize the 'name' attribute
    def __init__(self, name):
        self.name = name

    # Method of the base class   
    def printClassA(self):
        print("Class A Method")

# Intermediate class that inherits from class 'a'
class b(a):
    
    # Method of the intermediate class
    def printClassb(self):
        print("Class B Method")
        print("Name:", self.name)  # Accessing and printing the 'name' attribute inherited from the base class

# Derived class that inherits from class 'b'
class c(b):

    # Static method of the derived class
    @staticmethod
    def printClassC():
        print("Class C Method")

c_instance = c("Hello") # Creating an instance of the derived class 'c'
c_instance.printClassC() # Calling the static method of class 'c' using the instance
c_instance.printClassb() # Calling the method of class 'b' using the instance
c_instance.printClassA() # Calling the method of class 'a' using the instance of the derived class 'c'

'''
Example Of Multiple Inheritance
'''

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

# Derived class that inherits from class 'A' and class 'B'
class C(A, B): 
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)