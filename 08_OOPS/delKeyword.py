'''
del keyword are used to delte object properties or object itself
'''

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Krish") 
print(s1)
print(s1.name)

# Uncommenting the next two lines will delete the object 's1' and then trying to print 's1' will raise an error
# del s1
# print(s1) # Error: name 's1' is not defined because the object is deleted

del s1.name  # This deletes the 'name' attribute of the 's1' object
print(s1.name)  # Error: 'Student' object has no attribute 'name' because the 'name' attribute was deleted
