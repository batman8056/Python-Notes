# A class is a blueprint for creating objects. Objects are instances of a class, 
# which can have attributes (variables) and methods (functions).

class Person:
    def __init__(self, name, age):  # Constructor (initializer)
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance)
p1 = Person("John", 25)

# Accessing attributes and calling methods
print(p1.name)  # Output: John
print(p1.age)   # Output: 25
p1.greet()  # Output: Hello, my name is John and I am 25 years old.
