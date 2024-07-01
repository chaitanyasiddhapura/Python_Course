'''
Abstraction is used to hide the implementation details of a class and only show the essential features to the user.
'''

class car: 
    # Initialize the car's attributes: accelerator, brake, and clutch.
    # These details are hidden from the user.
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def carstart(self):
        # This method abstracts the complexity of starting the car.
        # Internally, it engages the clutch and the accelerator.
        self.clutch = True 
        self.acc = True 
        print("car start...") # User can see only this message; all other details are hidden.

# Create an instance of the car class.
carObj = car()
carObj.carstart()