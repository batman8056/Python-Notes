class Car:
    def __init__(self, brand="Toyota"):
        self.brand = brand

c1 = Car()  # Default value used
c2 = Car("Ford")

print(c1.brand)  # Output: Toyota
print(c2.brand)  # Output: Ford

# class Veicle:
#     def __init__(self, name):
#         self.name = name

# c1 =Veicle("bmw")

# print(c1.name)
