'''
Q1. Create Account class with 2 attributes - balance & account no.
Create method for debit, credit & printing the balance. 
'''

class Account:
     
    def __init__(self, accountNumber, balance):
        # Initialize the account with an account number and initial balance 
        self.accountNumber = accountNumber
        self.balance = balance

    # Method to debit an amount from the account
    def debit(self, debitAmount):
        self.balance -= debitAmount
        print("Your debited amount is:",debitAmount," and your current balance is ",self.balance)

    # Method to credit an amount to the account
    def credit(self, creditAmount):
        self.balance += creditAmount
        print("Your credit amount is:",creditAmount," and Your current balance is ",self.balance)

   # Method to print the current balance of the account
    def printBalance(self):
        print("Total Balance are: ", self.balance)

# Creating an instance of the Account class with account number and initial balance
a = Account(56498675419, 10000)

a.debit(500)
a.credit(5000)
a.printBalance()



