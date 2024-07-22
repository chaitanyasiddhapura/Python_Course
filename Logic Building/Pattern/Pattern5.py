'''
123
123
123
'''
n = 10
i = 1
# Outer loop for row 
while(i <= n):
    j = 1
    # Inner loop for column
    while(j <= n):
        print(j, end=" ") # Print the column value and keep the output on the same line 
        j = j + 1 # Increment the column value 
    print() # Move to the next line after completing a row
    i = i + 1 # Increment the row value




