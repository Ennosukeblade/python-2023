class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    @classmethod
    def display_all_accounts(cls):
        

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance} \nInterest Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1 + self.int_rate
        return self


account1 = BankAccount(0.01, 500)
account2 = BankAccount(0.05, 800)

account1.deposit(500).deposit(300).deposit(250).withdraw(200).yield_interest().display_account_info()
account2.deposit(300).deposit(250).withdraw(200).withdraw(600).withdraw(500).withdraw(100).display_account_info()
