'''
Constructor 
    All classes have a function called __init__(), Which is always executed when the object is being initiated.
'''

# Creating a class
class Student:
    # creating a Constructor
    def __init__(self):
        print("Hello, User")

s1 = Student()

'''
*The Self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class
'''

class StudentDetail:

    # default constructor
    def __init__(self):
       pass

    # Parameterized constructor
    def __init__(self, name, mark):
        self.name = name  
        self.mark = mark
        print("I am Parameterized constructor")


s1 = StudentDetail("Chaitanya", 85)
print(s1.name, s1.mark)   

s2 = StudentDetail("Krupal", 95)
print(s2.name, s2.mark)