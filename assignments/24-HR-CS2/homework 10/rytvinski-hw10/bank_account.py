class BankAccount:
    account_number = 0;
    owner_name = ""

    def __init__(self, account_number, owner_name):
        self.__balance = 0
        self.account_number = account_number
        self.owner_name = owner_name

    def deposit(self, value: float) -> bool:
        if value > 0:
            self.__balance += value
            return True
        
        return False
    
    def withdraw(self, value: float) -> bool:
        if value > 0 and value < self.__balance:
            self.__balance -= value
            return True
        
        return False
    
    def get_balance(self):
        return self.__balance
    

account1 = BankAccount(1, "Jhon Doe")
account1.deposit(1000)
account1.withdraw(30)
print(account1.get_balance())

account1 = BankAccount(2, "Jhon Snow")
account1.deposit(1300)
account1.withdraw(193)
print(account1.get_balance())



        
        
