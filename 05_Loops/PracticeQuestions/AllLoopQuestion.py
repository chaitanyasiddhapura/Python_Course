'''
Q1. Write a program to find sum of first n natural numbers.(Using while)
'''
# Initialize
sum = 0 
i = 1
n = int(input("Enter a Number: "))

# Use a while loop to add numbers from 1 to n
while(i <= n):
    sum += i  
    i = i + 1

# Print the sum of the first n natural numbers
print("The sum of N natural number: ",sum)


# Use FOR loop

n = int(input("Enter a Number: "))
sum = 0
# Use a for loop to add numbers from 1 to n
for i in range(1, n+1):
    sum += i

print("The sum of N number are: ", sum)



'''
Q2. Write a program to find the factorial of first n number.(Using for)
'''

# Initialize
i = 1
factorial = 1
n = int(input("Enter a Number: "))

# Use a for loop to multiply numbers from 1 to n
for i in range(1, n + 1):
    factorial *= i   # Multiply factorial by i

# Print the factorial of the number
print(factorial)


'''
Print a pattern
*
**
***
****
*****
'''
# Using for loop
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

# Using while loop
i = 0
while(i <= 5):
    j = 0
    while(j < i):
        print("*", end=" ")
        j += 1
    print()
    i += 1
