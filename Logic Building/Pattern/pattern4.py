'''
1
12
123
1234
12345
'''
# n = 5

# Get input from the user and store it in the variable 'n'
n = int(input("Enter a number: "))

i = 1
# loop to iterate from 1 to 'n'
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print() # Move to the next line after finishing the row
    i = i + 1