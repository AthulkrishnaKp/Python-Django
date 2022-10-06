class Bankaccount:
    def __init__(self):
        self.name=input("Enter the name of Depositor : ")
        self.ano=int(input("Enter the account number : "))
        self.type=input("Enter the Type of account : ")
        self.bal=0
        self.menu=print(" 1. Deposit ammount "
                        " 2. Withdraw ammount ")

    def deposit_Withdraw(self):
        self.input = int(input("Enter the Input : "))
        if self.input==1:
            d=int(input("Enter ammount to be deposited : "))
            self.bal=self.bal+d
        elif self.input==2:
            w=int(input("Enter the ammount to be withdrawn : "))
            if(self.bal>=w):
                self.bal=self.bal-w
                print("New balance : ",self.bal)
            else:
                print("Insufficient balance")
        else:
            print("Invalid input")

    def display(self):
        print("Name : ",self.name)
        print("Account name : ",self.ano)
        print("Account type : ",self.type)
        print("Balance : ",self.bal)

a=Bankaccount()
while 1:
    a.deposit_Withdraw()
    a.display()