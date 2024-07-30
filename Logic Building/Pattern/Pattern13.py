'''  
Printing a star pattern
'''

'''
   *
  **
 ***
****
'''

n = 4
i = 1

while i <= n:
    space = n - i  # Calculate the number of spaces to be printed before the stars in the current row
    # Print the space
    while(space):
        print(" ",end=" ")
        space = space - 1 
    j = 1
    # print a star (*)
    while(j <= i):
        print("*",end=" ")
        j = j + 1
    print()
    i = i + 1


print(" ") # Use for spareating a pattern 

'''
****
***
**
*
'''

n = 4
i = 1

while i <= n:
    j = 1
    StarPattern = n - i + 1  # Calculate the number of stars to be printed in the current row
    while j <= StarPattern:
        print("*",end=" ")
        j = j + 1
    print()
    i = i + 1


print(" ") # Use for spareating a pattern 

'''
****
 ***
  **
   *
'''


n = 4
i = 1

while i <= n:
    space = i - 1  # Calculate the number of spaces to be printed before the stars in the current row
    # Printing a space 
    while(space):
        print(" ",end=" ")
        space = space - 1
    j = 1

    star = n - i + 1 # Calculate the number of stars to be printed in the current row
    # Printing a star(*)
    while j <= star:
        print("*",end=" ")
        j = j + 1
    print()
    i = i + 1

print(" ") # Use for spareating a pattern 

'''
*
**
***
****
'''

n = 4
i = 1

while i <= n:
    j = 1
    while j <= i:
        print("*",end=" ")
        j = j + 1
    print()
    i = i + 1