class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

account1 = BankAccount("001", "Ann", 1000)
account2 = BankAccount("002", "Simon", 500)

account1.deposit(300)
account1.withdraw(200)
print(f"Ann's balance: {account1.get_balance()}")

account2.deposit(200)
account2.withdraw(800) 
print(f"Simon's balance: {account2.get_balance()}")
