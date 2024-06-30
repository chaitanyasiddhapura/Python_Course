'''
Static methods that don't use self parameter (work at class level)
'''

class Student:

    @staticmethod # decorator 
    def printHello():
        print("Hello")
    
s1 = Student()
s1.printHello()

'''
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
without permanently modifying it. 
'''