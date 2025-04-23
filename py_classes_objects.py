
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0


 # Instantiate an object from BankAccount Class blue print.
#my_account = BankAccount(15)
#my_account.withdraw(50)
#print (my_account.balance, my_account.overdrawn())
#my_account.deposit(150)
#print (my_account.balance, my_account.overdrawn())
#Ongeri Account
objOngeriAcc= BankAccount(10000)
print(objOngeriAcc.balance)
objOngeriAcc.withdraw(5000)
print((objOngeriAcc.balance))
print(objOngeriAcc.overdrawn())
objOngeriAcc.withdraw(7500)
print(objOngeriAcc.balance)
print((objOngeriAcc.overdrawn()))

objOnyangoAcc=BankAccount()
print(objOnyangoAcc.balance)
objOnyangoAcc.deposit(500)
print(objOnyangoAcc.balance)
print(objOnyangoAcc.overdrawn())

def deposit(amount):
    Balance=0;
    return Balance+amount;

print(deposit(1000))
print((objOnyangoAcc.balance))
print((objOngeriAcc.balance))
print(deposit(1))

