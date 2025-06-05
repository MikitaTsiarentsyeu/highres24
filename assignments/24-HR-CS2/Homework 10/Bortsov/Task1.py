class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"Ошибка: сумма пополнения должна быть положительной.")
            return
        self.__balance += amount
        print(f"Счет {self.account_number}: пополнение на {amount}. Текущий баланс: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Ошибка: сумма снятия должна быть положительной.")
            return
        if amount > self.__balance:
            print(f"Счет {self.account_number}: недостаточно средств для снятия {amount}. Баланс: {self.__balance}")
        else:
            self.__balance -= amount
            print(f"Счет {self.account_number}: снятие {amount}. Остаток: {self.__balance}")

    def get_balance(self):
        return self.__balance

acc1 = BankAccount("A1001", "Павел Петров", 1500)
acc2 = BankAccount("B2002", "Елена Кузнецова", 800)

acc1.deposit(450)
acc1.withdraw(300)
print(f"Баланс Павла: {acc1.get_balance()}")

acc2.deposit(150)
acc2.withdraw(1200)
print(f"Баланс Елены: {acc2.get_balance()}")
