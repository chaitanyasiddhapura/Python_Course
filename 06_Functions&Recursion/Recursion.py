'''
When a function calls itself repeatedly
'''

# Function for print n to 1 backwards
def printNumber(n):
    if(n == 0):
        return 
    print(n) # 5, 4, 3, 2, 1
    printNumber(n-1)

printNumber(5)


# Function for find factorial  
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return n * fact(n - 1)

output = fact(0)
print(output)