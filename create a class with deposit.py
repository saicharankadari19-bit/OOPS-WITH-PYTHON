class Bank:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Balance:",self.balance)
b = Bank(1000)
b.deposit(2000)
