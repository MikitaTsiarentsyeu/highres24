class bankAccount:
    def __init__(self, bankAccountID, bankAccountName):
        self._bankAccountID = bankAccountID
        self._bankAccountName = bankAccountName
        self._balance = 0

    def getBalance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            print("you cannot top up your account with a negative amount of money")
            return False
        else:
            self._balance += amount
            print(self._bankAccountName + " successfully deposited " + str(amount) + " $ to " + self._bankAccountID)
            print("current balance is " + str(self.getBalance()) + " $")
            return True


    def withdraw(self, amount):
        if self._balance < amount:
            print("you cannot withdraw more than your balance")
            return False
        elif amount < 0:
            print("you cannot withdraw negative amount of money from your account")
            return False
        else:
            self._balance -= amount
            print(self._bankAccountName + " successfully  withdrawn " + str(amount) + " $ from " + self._bankAccountID)
            print("current balance is " + str(self.getBalance()) + " $")
            return True

VasyaAccount = bankAccount("4692470","Vasya")
KatyaAccount = bankAccount("4829090","Katya")
OlegAccount = bankAccount("450070","Oleg")

print(VasyaAccount.getBalance())
print(VasyaAccount.withdraw(100))
print(VasyaAccount.getBalance())

print(KatyaAccount.deposit(100))
print(KatyaAccount.deposit(100))
print(KatyaAccount.withdraw(100))

print(OlegAccount.withdraw(100))
print(OlegAccount.deposit(-100))
print(OlegAccount.withdraw(-100))