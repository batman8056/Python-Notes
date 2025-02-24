# A class is a blueprint for creating objects. Objects are instances of a class, 
# which can have attributes (variables) and methods (functions).

class Person:
    def __init__(self, name, age):  # Constructor (initializer)
        self.name = name  # Stores the name attribute in the object.
        self.age = age    # Stores the age attribute in the object.

    def greet(self):  # Method inside the class.
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object p1 (instance)
p1 = Person("John", 25)

# Accessing attributes and calling methods
print(p1.name)  # Output: John
print(p1.age)   # Output: 25
p1.greet()  # Output: Hello, my name is John and I am 25 years old.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def msg(self):
#         print(f"Hello, my name is {self.name} and i am {self.age} years old.")
# a1= Student("manish", 27)
# a1.msg()