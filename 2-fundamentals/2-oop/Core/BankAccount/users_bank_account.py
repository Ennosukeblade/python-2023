# ------------------ bank account
class BankAccount:
    # Empty arr to store all accounts instances
    all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def display_all_accounts(cls):
        for a in cls.all_accounts:
            print(f"Balance: {a.balance}, Interest rate: {a.int_rate}")
        

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

# ------------------ user
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
        self.savingaccount = BankAccount(0.01, 750)
    
    def make_deposit(self, amount, acc = "main"):
        if acc == "main":
            self.account.deposit(amount)
        elif acc == "saving":
            self.savingaccount.deposit(amount)
        return self

    def make_withdrawal(self, amount, acc = "main"):
        if acc == "main":
            self.account.withdraw(amount)
        elif acc == "saving":
            self.savingaccount.withdraw(amount)
        return self

    def display_user_balance(self, acc = "main"):
        if acc == "main":
            print(self.account.balance)
        elif acc == "saving":
            print(self.savingaccount.balance)
        return self
    

user1 = User("Mouadh", "mouadhjenouiz@gmail.com")

user1.make_deposit(1000).make_withdrawal(150).display_user_balance()
user1.make_deposit(500, "saving").make_withdrawal(300, "saving").display_user_balance("saving")