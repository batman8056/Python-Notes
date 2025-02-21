# Class Method (@classmethod) - Works on Class Variable

class Employee:
    company = "Google"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company  # Modify class variable

Employee.change_company("Microsoft")
print(Employee.company)  # Output: Microsoft


# Static Method (@staticmethod) - No self or cls Needed (Acts like a normal function inside a class.)
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 10))  # Output: 15
