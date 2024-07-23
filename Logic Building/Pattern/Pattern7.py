'''
1
23
345
4567
'''

# Initialize the Variable 
n = 4
row = 1

# Logic 
while row <= n: # Print rows from 1 to n
    col = row  # Start at the current row number
    while col < row + row:
        print(col," ",end="")  # Print the number and stay on the same line
        col = col + 1
    print()
    row = row + 1