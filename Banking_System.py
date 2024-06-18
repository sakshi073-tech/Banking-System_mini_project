class BankAccount:
    def __init__(self,account_number,account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Deposited {amount}.New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}.New balance is {self.balance}")
        else:
            print(f"Withdrawal amount must be positive and with the available balance.")
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self,account_number,account_holder):
        BankAccount.__init__(self,account_number,account_holder)
        self.interest_rate = 0.02

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added.New balance is {self.balance}.")

class CheckingAccount(BankAccount):
    def __init__(self,account_number,account_holder):
        BankAccount.__init__(self,account_number,account_holder)

class BankingSystem:
    def __init__(self):
        self.account = {}
    def create_account(self,account_type,account_number,account_holder):
        if account_type =='savings':
            self.account[account_number]=SavingsAccount(account_number,account_holder)
        elif account_type == 'checking':
            self.account[account_number]=CheckingAccount(account_number,account_holder)
        else:
            print("Invalid account type.")
            return
        print(f"Account created for {account_holder} with number {account_number}.")

    def deposit(self,account_number,amount):
        if account_number in self.account:
            self.account[account_number].deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self,account_number,amount):
        if account_number in self.account:
            self.account[account_number].withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self,account_number):
        if account_number in self.account:
            balance = self.account[account_number].get_balance()
            print(f"The balance for account {account_number} is {balance}.")
        else:
            print("Account not found.")

    def add_interest(self,account_number):
        if account_number in self.account and isinstance(self.account[account_number],
            SavingsAccount):
            self.account[account_number].add_interest()
        else:
            print("Account not found or not a Savings account.")


    def run(self):

        while True:
            print("\n1: Create Account\n2: Deposit\n3: Withdraw\n4: Check Balance\n5: Add Interest (Savings Account Only)\n6: Exit")

            choice = int (input("Enter your choice :"))

            if choice == 1:
                account_type = input("Enter account type(savings/checking):").lower()
                account_number = input("Enter account number:")
                account_holder = input("Enter account holder name:")
                self.create_account(account_type,account_number,account_holder)

            elif choice == 2:
                account_number = input("Enter account number:")
                amount = float(input("Enter amount to deposit:"))
                self.deposit(account_number,amount)

            elif choice == 3:
                account_number = input("Enter account number:")
                amount = float(input("Enter amount to withdraw:"))
                self.withdraw(account_number,amount)

            elif choice == 4:
                account_number = input("Enter account number:")
                self.check_balance(account_number)

            elif choice == 5:
                account_number = input("Enter account number:")
                self.add_interest(account_number)

            elif choice == 6:
                break

            else:
                print("Invalid choice . Please try again,")


#instantiate the banking system and run it
banking_system = BankingSystem()
banking_system.run()













