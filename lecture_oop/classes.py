# simple class
class BankAccount:
    bank_name = 'Privat Bank'

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

vba = BankAccount(123, 100)
print(vba.balance)
vba.balance -= 5
vba.balance +=2
print(vba.balance)
print(type(vba))
#exit(0)

#### With methods
class BankAccount1:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print('Negatige amount')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        print(f"Account balance is {self.balance}.")

    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(
                f"Transferred {amount} to account {other_account.account_number}.")
        else:
            print("Insufficient balance.")

vba1 = BankAccount1(123, 100)
vba1.deposit(5)