'''
For n Size is 3
* * *
* * *
* * *
'''
# n = 3


n = int(input("Enter a number: ")) # User input 

# Loop through each row
for i in range(n):
    # Loop through each column
    for j in range(n): 
        print("*",end=" ") # Print "*" and a space on the same line
    print() # Move to the next line after printing all columns in the current row

