'''
Sum from 1 to n
'''

n = int(input("Enter a number: "))

# Using While loop
i = 1

SumN  = 0
while(i <= n):
    SumN = i + SumN
    i = i + 1

print(SumN)

# Using For loop


SumN = 0 
for i in range(n+1): # 0 to n so that (n + 1) 
    SumN = i + SumN

print(SumN)


