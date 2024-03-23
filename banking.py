import getpass

class Bank_Account:
    def __init__(self, user_name, password, balance):
        self.name = user_name
        self.password = password
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

# Function to create a list of Bank_Account objects
def create_bank_accounts(n):
    accounts = []
    for i in range(n):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        balance = float(input("Enter balance: "))
        account = Bank_Account(username, password, balance)
        accounts.append(account)
    return accounts

# Function to check username and password against created accounts
def authenticate_user(username, password, accounts):
    for account in accounts:
        if account.name == username and account.password == password:
            return account
    return None

# Taking input from user for no. of accounts
num_accounts = int(input("Enter the number of accounts to create: "))

# Creating bank accounts
total_accounts = create_bank_accounts(num_accounts)

#for task 1
#  Printing all created accounts
# print("\nAll accounts created:")
# for account in total_accounts:
#     print(account)

# Taking username and password from user for authentication
username_input = input("Enter your username to authenticate: ")
password_input = getpass.getpass("Enter your password: ")

# Checking which object the provided username and password belong to
for account in total_accounts:
    if account.name == username_input and account.password == password_input:
        print("The provided username and password belong to the following account:")
        print(account)
        break
else:
    print("No account found with the provided username and password.")