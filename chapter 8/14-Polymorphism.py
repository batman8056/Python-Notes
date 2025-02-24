# Same Method, Different Behavior
# Polymorphism allows the same method to have different behaviors based on the object calling it.
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# ✅ Polymorphic function
def animal_sound(animal):
    print(animal.make_sound())

# Usage
dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof! Woof!
animal_sound(cat)  # Meow!
