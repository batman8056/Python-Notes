# Hiding Implementation Details
# Abstraction is the process of hiding implementation details and showing only relevant functionalities using abstract classes.
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method, must be implemented by child classes

    @abstractmethod
    def stop_engine(self):
        pass  # Abstract method

# Concrete Class (Inheritance)
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started!"

    def stop_engine(self):
        return "Car engine stopped!"

# Usage
my_car = Car()
print(my_car.start_engine())  # Car engine started!
print(my_car.stop_engine())   # Car engine stopped!


# ✅ Vehicle is an abstract class, meaning it cannot be instantiated directly.
# ✅ Abstract methods (start_engine, stop_engine) force child classes to implement them.
# ✅ Hides unnecessary details and ensures implementation consistency.