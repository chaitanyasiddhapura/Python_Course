'''
Q1. Define a Circle class to create a circle with radius using the constructor.
Define an Area() method of the class which calculates the area of the Circle.
Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle. 
'''

class Circle:

    def __init__(self, radius):
        self.radius = radius 

    def Area(self):
        return 3.14 * self.radius * self.radius
    
    def Permeter(self):
        return 2 * 3.14 * self.radius

cOBJ= Circle(5)

print("Area Of The Circle:",cOBJ.Area())

print("Perimeter Of The Circle:",cOBJ.Permeter())


'''
Q2. Define a Employee class with attributes role, department & salary. this class  also a showDetails() method 
Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.
'''

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def  showDetails(self):
        print("Employee Role: ",self.role)
        print("Employee Department:",self.department)
        print("Employee Salary:",self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT", "78,788")

    
Engi1 = Engineer("Harsh", 24)
Engi1.showDetails()

'''
Q3. Create a class called Order which stores item & its price.
Use Dunder function __gt__() to convey that:
    order1 > order2 if price of order1 > price of order2
'''

class Oeder:
    def __init__(self, item, price):
        self.item = item
        self.price = price 

    def __gt__(self, odr2):
        return self.price > odr2.price 

odr1 = Oeder("Chips", 20)
odr2 = Oeder("tea", 15)

print(odr1 > odr2)