'''
 Prime Number Question
'''

n = int(input("Enter a number: "))
isPrime = 1
i = 2
while(i < n):
    if(n % i == 0):
        isPrime = 0
        break    
    i = i + 1

if(isPrime == 1):
    print("It's  prime")
else:
    print("It's not Prime")