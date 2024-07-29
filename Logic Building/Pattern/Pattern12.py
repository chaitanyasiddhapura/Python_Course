'''
Using chr() function 
D
CD
BCD
ABCD
'''

n = 4
i = 1

while i <= n:
    startingChar = 65 + n - i  # The ACSII value of A is 65 
    j = 1
    while j <= i:
        print(chr(startingChar), end=" ") # Convert ASCII value to character using chr() function and print 
        startingChar = startingChar + 1 
        j = j + 1
    print()
    i = i + 1  


'''
Using String 
D
CD
BCD
ABCD
'''

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = 4
i = 1

while i <= n:
    startingCharPossition = 0 + n - i # String start with 0 possition 
    j = 1
    while j <= i:
        print(alphabets[startingCharPossition], end=" ")
        startingCharPossition = startingCharPossition + 1
        j = j + 1
    print()
    i = i + 1

'''
Using chr() function 
ABC
BCD
CDE
'''

n = 3
i = 1

while i <= n:
    j = 1
    startingPossition = 65 + i - 1 # The ACSII value of A is 65 
    while j <= n:
        print(chr(startingPossition), end=" ") # Convert ASCII value to character using chr() function and print 
        startingPossition = startingPossition + 1
        j = j + 1
    print()
    i = i + 1


'''
Using String
ABC
BCD
CDE
'''

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = 3
i = 1

while i <= n:
    startingChar = 0 + i - 1 # String start with 0 possition 
    j = 1 
    while j <= n:
        print(alphabets[startingChar], end=" ") # Print the letter at the 'startingChar' position in 'alphabets', without moving to a new line
        startingChar = startingChar + 1
        j = j + 1
    print()
    i = i + 1

