'''
1111
 222
  33
   4
'''
n = 4
i = 1

while i <= n:

    space = i - 1 # Calculate the number of spaces to be printed before the numbers in the current row
    # Print the space 
    while(space):
        print(" ", end=" ")
        space = space - 1
    
    
    start = n - i + 1  # Calculate the number of times the current number should be printed in the current row
    j = 1
    # Print a number 
    while(j <= start):
        print(i,end=" ")
        j = j + 1

    print()
    i = i + 1


print()

'''
   1
  22
 333
4444
'''
n = 4
i = 1

while i <= n:
    
    space = n - i  # Calculate the number of spaces to be printed before the numbers in the current row
    # Print the space
    while(space):
        print(" ", end=" ")
        space = space - 1
    
    # print a number
    j = 1
    while j <= i:
        print(i, end=" ")
        j = j + 1
    print()
    i = i + 1


print()

'''
1234
 234
  34
   4
'''

n = 4
i = 1

while i <= n:
    
    # Print the space
    space = i - 1
    while(space):
        print(" ", end=" ")
        space = space - 1
    
    # Print a numbers
    j = 1
    temp_i = i
    start = n - i + 1

    while(j <= start):
        print(temp_i,end=" ")
        temp_i = temp_i + 1 
        j = j + 1
    print()
    i = i + 1

print()

'''
   1
  23
 456
78910
'''

n = 4
count = 1
i = 1

while i <= n:

    # Print the space
    space = n - i
    while(space):
        print(" ",end=" ")
        space = space - 1

    # print the number 
    j = 1
    while(j <= i):
        print(count,end=" ")
        count = count + 1
        j = j + 1
    print()
    i = i + 1  