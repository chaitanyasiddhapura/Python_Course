'''
Super() method is used to access methods of the parent class. 
'''

class Car:
    # Constructor to initialize the type of car
    def __init__(self, type):
        self.type = type 
    
    # Static method to start the car
    @staticmethod
    def start():
        print("Car Start")
    
    # Method to stop the car
    def stop():
        print("Car Stop")

# Define a child class named ToyotaCar that inherits from Car
class ToyotaCar(Car):
    # Constructor to initialize the name and type of the Toyota car
    def __init__(self, name, type): 
        super().__init__(type) # Call the parent class's constructor to initialize the type
        self.name = name
        super().start()  # Call the parent class's start method
    
# Create an instance of ToyotaCar with name "Prius" and type "Electric"
Car1 = ToyotaCar("Prius", "Electric")
print(Car1.type)