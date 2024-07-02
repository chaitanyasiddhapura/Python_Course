'''
Encapsulation are use for wrapping data and function into a single unit(object)
'''

class Car:
    def __init__(self, company, model):
        self.company = company   # Public attribute for the car's company
        self.model = model  # Private attribute for the car's model with double underscore prefix

    def display_details(self):
        # Public method to display car details
        print("Car:", self.company,", Model:", self.model)

    def change_model(self, new_model):
        # Public method to change the car's model
        self.model = new_model

# Creating an object of the Car class
my_car = Car("TATA", "Punch")

# Accessing public method to display details
my_car.display_details() 