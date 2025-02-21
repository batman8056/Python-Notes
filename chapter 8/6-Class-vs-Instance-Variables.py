# company (class variable) is shared across all instances.
# name (instance variable) is unique to each instance.

class Employee:
    company = "Google"  # Class variable (shared by all instances)

    def __init__(self, name):
        self.name = name  # Instance variable (unique to each object)

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)  # Output: Google
print(e2.company)  # Output: Google

Employee.company = "Microsoft"  # Changing class variable
print(e1.company)  # Output: Microsoft
print(e2.company)  # Output: Microsoft
