class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number  
        self.owner_name = owner_name          
        self._balance = balance             
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Внесено {amount}. Новый баланс: {self._balance}")
        else:
            print("Сумма должна быть положительной!")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Снято {amount}. Новый баланс: {self._balance}")
            else:
                print("Недостаточно средств на счете!")
        else:
            print("Сумма должна быть положительной!")
    
    def get_balance(self):
        return self._balance

account1 = BankAccount("12345", "Иван Иванов", 1000)
account2 = BankAccount("67890", "Анна Петрова", 500)

print(f"Счет {account1.account_number} ({account1.owner_name}):")
print("Начальный баланс:", account1.get_balance())
account1.deposit(500)   
account1.withdraw(200)  
account1.withdraw(2000) 


print(f"\nСчет {account2.account_number} ({account2.owner_name}):")
print("Начальный баланс:", account2.get_balance())
account2.deposit(1000)  
account2.withdraw(300)  
account2.deposit(-50)   