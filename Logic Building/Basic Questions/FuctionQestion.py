# Q1) Calculating a power
def power(num1 : int, num2 : int) -> int:
    ans = 1
    for i in range(num2):
        ans = ans * num1
    
    return ans


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
ans = power(num1, num2)
print(ans)

# Q2) Find nCr

'''
Logic:
n = 8, r = 2

n! = 1*2*3*4*5*6*7*8
r! = 1*2
(n-r)! = n - r 
       = 8 - 2
       = 6
(n-r)! = 6! -> 1*2*3*4*5*6
'''

def factu(n):
    
    i, fact = 1, 1
    
    while(i <= n):
        fact = i * fact
        i = i + 1
    
    return fact
    
def ncr(n, r):
    
    num = factu(n)
    divide = factu(r)*factu(n-r)
    ncr = num / divide
    
    return ncr 
    
ans = ncr(10, 2)
print(ans)



# Q3) print counting

def countNum(n):
    i = 1
    while(i <= n):
        print(i, end=" ")
        i = i + 1

countNum(5)
print()
# Q4) check prime or not


def isPrime(n):

    for i in range(2, n):
        if(n%i==0):
            return 0
    
    return 1

n = int(input("Enter a number: "))
if(isPrime(n)):
    print(n," is prime number")    
else:
    print(n," is not prime number")