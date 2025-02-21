# self represents the instance of the class.
# It is used to access attributes and methods inside the class.
# Without self, Python won't know which object's data to access.

class Example:
    def say_hello(self):
        print("Hello!")

obj = Example()
obj.say_hello()  # Output: Hello!
