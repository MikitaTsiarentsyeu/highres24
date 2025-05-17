class BankAccount:
    def __init__(self, start):
        self.__balance = start

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}.")
        else:
            print("Not enough funds.")

    def get_balance(self):
        print(f"Current balance: {self.__balance}")

account1 = BankAccount(300)
account2 = BankAccount(700)
account3 = BankAccount(1500)

print("\nAccount 1")
account1.deposit(150)
account1.withdraw(100)
account1.get_balance()

print("\nAccount 2")
account2.withdraw(300)
account2.deposit(50)
account2.get_balance()

print("\nAccount 3")
account3.withdraw(250)
account3.get_balance()