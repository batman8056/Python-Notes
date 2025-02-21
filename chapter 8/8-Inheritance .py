# Single Inheritance → One parent, one child.
# Multiple Inheritance → A child class inherits from multiple parent classes.
# Multilevel Inheritance → Grandparent → Parent → Child.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")

d = Dog()
d.speak()  # Output: Animal speaks (inherited)
d.bark()   # Output: Woof!
