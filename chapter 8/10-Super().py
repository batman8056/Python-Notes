# Super() - Calling Parent Class Methods
# super().__init__(name) → Calls parent's constructor.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

d = Dog("Buddy", "Golden Retriever")
print(d.name)   # Output: Buddy
print(d.breed)  # Output: Golden Retriever
