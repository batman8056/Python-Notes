# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# c = Circle(5)
# print(c.area())  # Output: 78.5


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2 
        
obj1 = Circle(4)
print(obj1.area())