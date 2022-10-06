class Bankaccount:
    def __init__(self):
        self.name=input("Enter the name of Depositor : ")
        self.ano=int(input("Enter the account number : "))
        self.type=input("Enter the Type of account : ")
        self.bal=int(input("Enter the Balance ammount : "))
    def display(self):
        print("Name of depositor : ",self.name)
        print("Account number : ",self.ano)
        print("Type of account : ",self.type)
        print("Balance ammount : ",self.bal)
class Deposit(Bankaccount):
    def __init__(self):
        Bankaccount.display(self)
        self.depo=int(input("Enter ammount to be deposited : "))
        self.bal=self.depo+self.bal
        Bankaccount.display(self)
class Withdraw(Deposit):
    def __init__(self):
        Bankaccount.__init__(self)
        Deposit.__init__(self)
        self.wdraw=int(input("Enter the ammount to be withdrawn : "))
    def displaybalance(self):
        self.bal=self.bal-self.wdraw
        Bankaccount.display(self)

a=Withdraw()
a.displaybalance()