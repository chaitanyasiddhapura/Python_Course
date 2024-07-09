'''
We use @property decorator on any method in the class to use the method as a property.
'''

class Student:
    # Constructor to initialize the marks in physics, chemistry, and math
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem 
        self.math = math

    # Property to calculate and return the percentage of marks
    @property
    def percentage(self):
        return str((self.phy + self.chem +  self.math) / 3) + "%"

# Create an instance of the Student class with marks 89, 97, and 99
stu1 = Student(89,97,99)

print(stu1.percentage) # Print the percentage of marks
stu1.phy = 98 # Change the physics mark to 98
print(stu1.phy) # Print the updated physics mark
print(stu1.percentage) # Print the updated percentage of marks
