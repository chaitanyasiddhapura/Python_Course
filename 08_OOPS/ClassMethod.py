'''
A class method is bound to the class & receives the class as an implicit first argument
* Static method can't access or modify class state & generally for utility.
'''


class Person:
    # Class attribute to hold the name, default is "anonymous"
    name = "anonymous"

    # Instance method to change the class attribute name
    # def changeName(self, name):
    #     self.__class__.name = name


    # Class method to change the name attribute of the class
    @classmethod # decorator
    def changeName(ClassRef, name):
        # Update the class attribute name with the new name
        ClassRef.name = name


p1 = Person()
p1.changeName("Madhav") # Call the class method changeName to change the class attribute name to "Madhav"
print(p1.name) # Print the name attribute of the instance p1
print(Person.name) # Print the name attribute of the Person class
