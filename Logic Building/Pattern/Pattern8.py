'''
1 
21 
321
4321
'''
# Initialize the Variable 
n = 4
row = 1 

# Logic 

while row <= n:
    col = row  # Initialize the column value to the current row
    while col >= 1:
        print(col," ", end="")  # Print column value and stay on the same line
        col = col - 1  # Decrement the column value to print in decreasing order  
    print() # for new line 
    row = row + 1 # Increment the row value to process the next row
