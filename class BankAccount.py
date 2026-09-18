class BankAccount:
    def __init__(self,Acc_Holder,Acc_No,Balance):
        self.Acc_Holder=Acc_Holder
        self.Acc_No=Acc_No
        self.Balance=Balance
    def deposit(self,amount):
        #amount=int(input())
        self.Balance += amount
        print(self.Balance)
    def withdrawl(self,cash):
        self.Balance -= cash
        print(cash)
    def check_Balance(self):
        print(self.Balance)


A1=BankAccount("sai","ASDHG23",30000)
A1.deposit(300)
A1.withdrawl(300)
A1.check_Balance()

        
            
        
