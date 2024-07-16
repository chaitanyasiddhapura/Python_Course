'''
*
**
***
****
*****
'''

userInput = int(input("Enter a number: "))
i = 0
while i < userInput:
    j = 0  # Reset j for each new row
    while j <= i:
        print("*", end="")
        j += 1
    print()  # Move to the next line after finishing the row
    i += 1
