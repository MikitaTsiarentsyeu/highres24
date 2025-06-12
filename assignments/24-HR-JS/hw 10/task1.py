class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = initial_balance
        self.__transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +${amount:.2f}")
        return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawal: -${amount:.2f}")
        return f"Withdrawn ${amount:.2f}. New balance: ${self.__balance:.2f}"

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        return {
            "account_number": self.__account_number,
            "owner_name": self.__owner_name,
            "balance": self.__balance
        }

    def get_transaction_history(self):
        return self.__transaction_history

def main():
    try:
        account1 = BankAccount("1234567890", "John Doe", 1000)
        account2 = BankAccount("0987654321", "Jane Smith", 500)

        print("=== Account 1 Operations ===")
        print(account1.deposit(500))
        print(account1.withdraw(200))
        print(f"Current balance: ${account1.get_balance():.2f}")

        print("\n=== Account 2 Operations ===")
        print(account2.deposit(1000))
        print(account2.withdraw(300))
        print(f"Current balance: ${account2.get_balance():.2f}")

        print("\n=== Account Information ===")
        print("Account 1:", account1.get_account_info())
        print("Account 2:", account2.get_account_info())

        print("\n=== Transaction History ===")
        print("Account 1 transactions:", account1.get_transaction_history())
        print("Account 2 transactions:", account2.get_transaction_history())

        print("\n=== Error Handling ===")
        try:
            account1.withdraw(2000)
        except ValueError as e:
            print(f"Error: {str(e)}")

        try:
            account2.deposit(-100)
        except ValueError as e:
            print(f"Error: {str(e)}")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()