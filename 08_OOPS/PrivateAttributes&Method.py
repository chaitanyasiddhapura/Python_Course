'''
Private Attributes & Methods are meant to be used only within the class and are not accessible from outside the class.
'''

class Account:

    def __init__(self, accountNo, Password):
        # Public attribute for account number
        self.accountNo = accountNo
          # Private attribute for password (not accessible from outside the class, defined with __ (double underscores)
        self.__Password = Password
 
    def userName(self, name):
        # Public method that calls a private method to print a welcome message
        self.__printWelcome(name)
 
    # Private Method (not accessible from outside the class)
    def __printWelcome(self, name):
        print("Welcome",name)


# Create an Account object with account number and password
a = Account(649865949819,"bfywsd498984949")
print("Account Number: ",a.accountNo) # Print the account number (public attribute)
# print("User password: ",a.Password) # Attempt to print the password (will cause an error because it's private)
a.userName("Chaitanya") # Call the public method to print a welcome message 

