# Private variables (__balance) cannot be accessed directly outside the class.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance  # Access private variable

acc = BankAccount(1000)
print(acc.get_balance())  # Output: 1000
