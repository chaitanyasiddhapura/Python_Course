'''
Q1. Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average
'''

class Student:

    def __init__(self, Name, marks):
        self.Name = Name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hey,", self.Name, "Your avg score is: ", sum / 3 )
s1 = Student("Yash",[87, 56, 88])
s1.get_avg()