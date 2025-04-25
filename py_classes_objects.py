
class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
    def securitycheck(self):
        status=False;
        setpin="3020"
        chances=3;
        while chances!=0:
            pin = input("Enter pin " +str( chances) + " tries remain \n")
            if pin==setpin:
                status=True;
                print(" Access granted")
                self.selfservice();
                break;

            chances=chances-1;

            #print("Enter Pin again. " +chances % + "tries remain")
        return status;
    def selfservice(self):
        service = ""
        #secure=self.securitycheck()
        #if (secure == True):
        print('To Deposit Enter 1')
        print('To Withdraw Enter 2')
        print('To check balance Enter 3')
        service = input("Choose your service please..")
        if service == 'd' or 'D':
            amount = input("Enter deposit amount: \n")
            self.deposit(amount)
            print(self.balance)
        elif service == 'w' or 'W':
            amount = input((" Enter withdrawal amount \n"))
            self.withdraw(amount)
            print(self.balance())
            ...


 # Instantiate an object from BankAccount Class blue print.
#my_account = BankAccount(15)
#my_account.withdraw(50)
#print (my_account.balance, my_account.overdrawn())
#my_account.deposit(150)
#print (my_account.balance, my_account.overdrawn())
#Ongeri Account
objOngeriAcc= BankAccount(10000)
amount=0;
#userpin=input("Enter Pin ****\n")
secure=objOngeriAcc.securitycheck()


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

