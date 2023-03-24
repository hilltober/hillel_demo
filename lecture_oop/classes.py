# simple class
class BankAccount:
    bank_name = 'Monobank'

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


vba = BankAccount(123, 100)
print(vba.balance)
vba.balance -= 5
vba.balance += 2
print(vba.balance)
print(type(vba))


# exit(0)

# With methods
class BankAccount1:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        elif amount == 0:
            print(f'Deposited nothing. Balance still {self.balance}.')
        else:
            print('Negative amount')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is {self.balance}.")
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
vba2 = BankAccount1(124, 100)
vba1.deposit(5)
vba1.transfer(vba2, 50)
vba1.get_balance()
vba2.get_balance()


class A:
    result = 1


class B(A):
    def __init__(self):
        result = 2


class C(B):
    def __init__(self):
        self.result = 3


class D(C):
    result = 4


print(A.result)
print(B.result)
print(C.result)
print(D.result)

print(A().result)
print(B().result)
print(C().result)
print(D().result)
