# i decided to do homework 10

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money.")

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("001", "Alice", 100)
acc2 = BankAccount("002", "Bob", 50)


acc1.deposit(50)
acc1.withdraw(30)
print("Alice's balance:", acc1.get_balance())

acc2.deposit(20)
acc2.withdraw(100)
print("Bob's balance:", acc2.get_balance())