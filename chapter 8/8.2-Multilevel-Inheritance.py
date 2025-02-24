# Base Class (Grandparent)
class Animal:
    def breathe(self):
        return "I can breathe"

# Intermediate Class (Parent)
class Mammal(Animal):
    def feed_milk(self):
        return "I can feed milk"

# Derived Class (Child)
class Dog(Mammal):
    def bark(self):
        return "Woof! Woof!"

# Creating an object of Dog
dog = Dog()

# Accessing methods from all levels
print(dog.breathe())  # Output: I can breathe (from Animal class)
print(dog.feed_milk()) # Output: I can feed milk (from Mammal class)
print(dog.bark())      # Output: Woof! Woof! (from Dog class)
