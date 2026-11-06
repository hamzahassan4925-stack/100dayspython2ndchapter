class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc

    def debit(self, amount):
        self.balance -= amount   
        print("rs", amount,"was debited from your account") 

    def credit(self, amount):
        self.balance += amount
        print("rs", amount,"was credited to your account")

    def getbalance(self):
        return self.balance
    
acc1 = Account(1000, "123456789")      
acc1.debit(184)
acc1.credit(500)
print(acc1.balance)
print(acc1.account_number)