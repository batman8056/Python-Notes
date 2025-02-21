class Person:
    def __init__(self, name, age):  # Constructor (initializer)
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance)
p1 = Person("John", 25)
p1.age = 35  # Modify attribute
print(p1.age)  # Output: 35
