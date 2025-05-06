class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc1 = BankAccount("123456", "Alice", 500)
acc1.deposit(200)
acc1.withdraw(100)
print(acc1.get_balance())

acc2 = BankAccount("654321", "John", 750)
acc2.deposit(180)
acc2.withdraw(120)
print(acc2.get_balance())