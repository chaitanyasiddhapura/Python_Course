'''
Binary To Decimal
'''

# User Input
n = int(input("Enter a number: "))

# Initialize variables
i = 0
ans = 0

# Logic 
while(n != 0):
    digit = n % 10 # Extract the last digit

    if(digit == 1): # Check if the digit is 1
        ans = ans + pow(2, i) # Add 2^i to the result
    
    n = int(n / 10) # Remove the last digit from the number
    i = i + 1

print(ans) # Print the final result