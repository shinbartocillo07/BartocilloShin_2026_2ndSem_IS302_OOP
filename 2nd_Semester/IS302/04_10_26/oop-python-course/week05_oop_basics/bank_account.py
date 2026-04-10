class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name_SGB = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.balance)


account = BankAccount("Juan", 5000)
account.deposit(1000)
account.withdraw(2000)
account.display_balance()
