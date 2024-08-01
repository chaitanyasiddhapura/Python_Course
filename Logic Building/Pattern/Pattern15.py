'''
   1
  121
 12321
1234321
'''

n = 4
i = 1

while(i <= n):
    # space
    space = n - i
    while(space):
        print(" ", end=" ")
        space = space - 1

    # print number
    j = 1 
    while(j <= i):
        print(j,end=" ")
        j = j + 1
    
    temp = i - 1
    while(temp > 0):
        print(temp,end=" ")
        temp = temp - 1

    print()
    i = i + 1 

'''
   *
  ***
 *****
*******
'''
# Logic-1
n = 4
i = 1

while(i <= n):
    # space
    space = n - i
    while(space):
        print(" ", end=" ")
        space = space - 1

    # print number
    j = 1 
    while(j <= i):
        print("*",end=" ")
        j = j + 1
    
    temp = i - 1
    while(temp > 0):
        print("*",end=" ")
        temp = temp - 1

    print()
    i = i + 1 


# Logic-2

n = 4 
i = 1

while i <= n:
    # space
    j = i
    while(j <= n):
        print(" ", end=" ")
        j = j + 1   
    k = 1
    while(k <= (2*i-1)):
        print("*",end=" ")
        k = k + 1
    print()
    i = i + 1