class Bank_Account:
    def __init__(self,user_name,password,balance):
        self.name=user_name
        self.password=password
        self.balance=balance
    
    def withdraw(self,amount):
        self.balance-=amount

    def deposit(self,amount):
        self.balance+=amount

object_1=Bank_Account('ABC','password',float('500000'))
print(object_1.name,object_1.password,object_1.balance)


object_2=Bank_Account('XYZ','password',float('000000'))
print("Before Withdraw")
print(object_2.name,object_2.password,object_2.balance)

print("After Withdraw")
object_2.withdraw(400)
print(object_2.name,object_2.password,object_2.balance)