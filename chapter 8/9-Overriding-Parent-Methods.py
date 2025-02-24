class Animal:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def speak(self):  # Overriding parent method
        print("Meow!")

c = Cat()
c.speak()  # Output: Meow!
