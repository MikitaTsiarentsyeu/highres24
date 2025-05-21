class bankAccount:
    def __init__(self, account_number, owner_name):
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            return False
        else:
            self._balance += amount

    def withdraw(self, amount):
        if (self._balance < amount) or (amount < 0):
            return False
        else:
            self._balance -= amount
