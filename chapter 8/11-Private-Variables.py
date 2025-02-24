# Private variables (__balance) cannot be accessed directly outside the class.
# In Python, variables prefixed with _ (single underscore) or __ (double underscore) are considered private (though not strictly enforced).
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable(Encapsulation)

    def get_balance(self):
        return self.__balance  # Access private variable

acc = BankAccount(1000)
print(acc.get_balance())  # Output: 1000
