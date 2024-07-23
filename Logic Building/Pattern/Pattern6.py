'''
321
321
321

Here the logic Hint..,
Suppose j(column) value respective 1, 2, 3 
n - j + 1 
3 - 1 + 1 = 3
3 - 2 + 1 = 2
3 - 3 + 1 = 1

'''

n = 3
i = 1 # Row start with 1 index 
# Outer loop for row element  
while i <= n: 
    j = 1 # Column start with 1 index 
    # Inner loop for column element 
    while j <= n:
        print(n - j + 1, end="") # Calculate and print the value like this 321
        j = j + 1
    print() # For new line 
    i = i + 1

