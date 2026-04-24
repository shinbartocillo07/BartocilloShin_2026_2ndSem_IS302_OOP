class BankAccount_nbs:
    def __init__(self_SGB, balance_SGB):
        self_SGB.__balance_SGB = balance_SGB

    def deposit_SGB(self_SGB, amount_SGB):
        self_SGB.__balance_SGB += amount_SGB

    def withdraw_SGB(self_SGB, amount_SGB):
        if amount_SGB <= self_SGB.__balance_SGB:
            self_SGB.__balance_SGB -= amount_SGB
        else:
            print("Insufficient funds")

    def get_balance_SGB(self_SGB):
        return self_SGB.__balance_SGB

account_SGB = BankAccount_SGB(5000)
account_SGB.deposit_SGB(1000)
account_SGB.withdraw_SGB(2000)
print("Balance_SGB:", account_SGB.get_balance_SGB())