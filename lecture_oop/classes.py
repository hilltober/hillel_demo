# # simple class
# class BankAccount:
#     bank_name = 'Monobank'
#
#     def __init__(self, account_number: int = None, balance: int = None, name=None):
#         self.account_number = account_number
#         self.balance = balance
#         if name:
#             self.bank_name = name
#
#
# print(BankAccount.bank_name)
# print(BankAccount().bank_name)
#
# # vba = BankAccount(123, 100)
# # print(vba.balance)
# # vba.balance -= 5
# # vba.balance += 2
# # print(vba.balance)
# # print(type(vba))


# exit(0)
#
# With methods
class BankAccount:
    def __init__(self, account_number: int, balance: int):
        self.account_number = account_number
        self.balance = balance
        self.cls = self.__class__.__name__

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        elif amount == 0:
            print(f'Deposited nothing. Balance still {self.balance}.')
        else:
            print('Negative amount')

    def withdraw(self, amount: int) -> None:
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def get_balance(self) -> int:
        print(f"Account {self.account_number} balance is {self.balance}.")
        return self.balance

    def transfer(self, other_account: 'BankAccount', amount: int) -> None:
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(
                f"Transferred {amount} to account {other_account.account_number}.")
        else:
            print("Insufficient balance.")


account_1 = BankAccount(1, 100)
account_2 = BankAccount(2, 250)

account_1.deposit(100)
account_1.get_balance()
account_1.transfer(account_2, 100)
account_1.get_balance()
account_2.get_balance()
