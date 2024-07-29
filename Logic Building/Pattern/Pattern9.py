'''
ABC
ABC
ABC
'''

# Get the number of lines to print from the user
n = int(input("Enter a number: "))
# n = 3
i = 1

# Outer loop for the number of rows
while(i <= n):
    j = 1
    # Inner loop for the number of columns
    while(j <= n):
        ch = 65 + j-1 # ASCII value of 'A' is 65
        print(chr(ch), end = " ") # Convert ASCII value to character using chr() function and print 
        j = j + 1
    print()
    i = i + 1

print("*****")

'''
Without using function like 'chr'

ABC
ABC
ABC
'''
# This code might cause an error if n is 27 or higher value because the String index is out of range.


# n = 3

i = 1 
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while(i <= n):
    j = 1
    while(j <= n):
        ch = alphabets[j - 1]  # Get the character from the string
        print(ch, end=" ")
        j = j + 1
    print()
    i = i + 1

print("*****")

'''
Using array print parrten 

ABC
ABC
ABC 
'''

# This code might cause an error if n is 27 or higher value because the list index is out of range.


# n = 3 
alphabetsList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # Define the list of characters
i = 1

while(i <= n):
    j = 1
    while(j <= n):
        ch = alphabetsList[j - 1] # Get the character from the list
        print(ch, end=" ")
        j = j + 1
    print()
    i = i + 1


