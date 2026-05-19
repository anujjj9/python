# Base class
class Vehicle:
    # Generic method defined in the parent class
    def start(self):
        print("Vehicle starts")

# Child class inheriting from Vehicle
class Car(Vehicle):
    # Overriding the 'start' method with Car-specific behavior
    def start(self):
        print("Car starts with a key")

# Another child class inheriting from Vehicle
class Bike(Vehicle):
    # Overriding the 'start' method with Bike-specific behavior
    def start(self):
        print("Bike starts with a kick")


# Polymorphism in action WITHOUT loops:
# Each object calls its own version of the 'start' method.

car_obj = Car()      # Create a Car object
car_obj.start()      # Calls Car's overridden start()

bike_obj = Bike()    # Create a Bike object
bike_obj.start()     # Calls Bike's overridden start()
