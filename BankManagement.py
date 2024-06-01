# We are going to make a Bank Management
# System. This will mean that I will have
# Users create an account, deposit, withdraw,
# and check their balance.

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user):
        if user not in self.accounts:
            self.accounts[user] = 0  # Initialize account with 0 balance
            print(f"Account created for {user}")
        else:
            print(f"{user} already has an account")

    def deposit(self, user, amount):
        if user in self.accounts:
            self.accounts[user] += amount
            print(f"Deposited {amount} to {user}'s account")
        else:
            print(f"No account for {user}")

    def withdraw(self, user, amount):
        if user in self.accounts:
            if self.accounts[user] >= amount:
                self.accounts[user] -= amount
                print(f"{user} withdrew {amount}")
            else:
                print(f"Not enough money in the account")
        else:
            print(f"No account for {user}")

    def check_balance(self, user):
        if user in self.accounts:
            return self.accounts[user]
        else:
            return "Account does not exist"

def main():
    bank = Bank()  # Create an instance of Bank
    bank.create_account("Myranda")  # Create an account for My
    bank.deposit("Myranda", 1000)  # Deposit 1000 to My account
    bank.withdraw("Myranda", 500)  # Withdraw 500 from My account
    balance = bank.check_balance("Myranda")  # Check My balance
    print(f"Myranda's balance: {balance}")

if __name__ == "__main__":
    main()