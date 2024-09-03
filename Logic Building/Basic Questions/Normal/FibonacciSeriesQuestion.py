'''
Fibonacci Series 
'''

'''
Using While loop
'''

# Initilize
n = int(input("Enter a number: "))
a = 0 
b = 1

print(a, b, end=" ") # print the starting value 0 and 1

# Logic
i = 1
while(i <= n): # loop upto n number
    nextNumber = a + b # Add a and b to get the next number
    print(nextNumber,end=" ")  # Print the next number
    a = b # Move the current number (b) to a
    b = nextNumber # Update b with the new number 
    i = i + 1    # Increase the value of i by 1


print() # sperating while and for loop code Output

'''
Using For Loop
'''
# Initializing Again beasuce value of a and b are change
a = 0 
b = 1

print(a, b, end=" ")

for i in range(n): # loop upto n number
    nextNumber = a + b
    print(nextNumber,end=" ")
    a = b 
    b = nextNumber


