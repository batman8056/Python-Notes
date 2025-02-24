# Parent Class 1
class Engine:
    def start(self):
        return "Engine started"

# Parent Class 2
class Wheels:
    def rotate(self):
        return "Wheels are rotating"

# Child Class (Inheriting from both Engine and Wheels)
class Car(Engine, Wheels):
    def drive(self):
        return "Car is driving"

# Creating an object of Car
my_car = Car()

# Accessing methods from both parent classes
print(my_car.start())   # Output: Engine started (from Engine class)
print(my_car.rotate())  # Output: Wheels are rotating (from Wheels class)
print(my_car.drive())   # Output: Car is driving (from Car class)
