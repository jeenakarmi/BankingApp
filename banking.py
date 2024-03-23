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

# Function to create a list of Bank_Account objects (for 1)
def create_bank_accounts(n):
    accounts = []
    for i in range(n):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        balance = float(input("Enter balance: "))
        account = Bank_Account(username, password, balance)
        accounts.append(account)
    return accounts

# Function to check username and password against created accounts (for 2 and 3)
def authenticate_user(username, password, accounts):
    for account in accounts:
        if account.name == username and account.password == password:
            return account
    return None

# Function to find account by username (for 4)
def find_account(accounts, username):
    for account in accounts:
        if account.name == username:
            return account
    return None

# Taking input from user for no. of accounts 
num_accounts = int(input("Enter the number of accounts to create: "))

# Creating bank accounts
total_accounts = create_bank_accounts(num_accounts)

'''
#for task 1
# Printing all created accounts
    print("\nAll accounts created:")
for account in total_accounts:
    print(account)
'''

# For 2 and 3

# Taking username and password from user for authentication
username_input = input("Enter your username to authenticate: ")
password_input = getpass.getpass("Enter your password: ")

'''
# Checking which object the provided username and password belong to
# for account in total_accounts:
#     if account.name == username_input and account.password == password_input:
        # for task 2
        # print("The provided username and password belong to the following account:")
        # print(account)

        # for task 3
        # print("Account Information:")
        # print("Username:", account.name)
        # print("Password:", account.password)
        # print("Balance:", account.balance)

#         break

# else:
#     print("No account found with the provided username and password.")

'''

# for task 4 5 6
# If authentication successful, proceed to transfer money
# Authenticating user
authenticated_account = None
for account in total_accounts:
    if account.name == username_input and account.password == password_input:
        authenticated_account = account
        break

# If authentication successful, proceed to transfer money
if authenticated_account:
    recipient_username = input("Enter the username of the recipient: ")
    recipient_account = find_account(total_accounts, recipient_username)
    
    if recipient_account:
        amount = float(input("Enter the amount to transfer: "))
        if amount <= authenticated_account.balance:
            authenticated_account.withdraw(amount)
            recipient_account.deposit(amount)
            print("Transfer successful!")
        else:
            print("Insufficient balance.")
    else:
        print("Recipient account not found.")
else:
    print("Authentication failed. Invalid username or password.")