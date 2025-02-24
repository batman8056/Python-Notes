class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable (Encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New Balance: {self.__balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Remaining Balance: {self.__balance}"
        return "Insufficient funds or invalid amount!"

    def get_balance(self):  # Public method to access private variable
        return f"Current Balance: {self.__balance}"

# Usage
acc = BankAccount(1000)
print(acc.deposit(500))  # Deposited 500. New Balance: 1500
print(acc.withdraw(200))  # Withdrew 200. Remaining Balance: 1300
print(acc.get_balance())  # Current Balance: 1300

# Trying to access private variable directly (will fail)
# print(acc.__balance)  # AttributeError
