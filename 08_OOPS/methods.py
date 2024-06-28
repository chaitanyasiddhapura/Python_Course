'''
Methods are function that belong to objects.
'''

# Creating class  
class student:
    collegeName = "ABC College"

    def __init__(self, name, mark):
        self.name = name 
        self.mark = mark

    # Welcome the students
    def Welcome(Self):
        print("Welcome",end = " ")

    # Printing name of student
    def getName(Self):
        return Self.name

s1 = student("Chaitanya", 98)
s1.Welcome()
print(s1.getName())


