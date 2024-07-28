'''
A
BC
DEF
GHIJ
'''

n = 4
i = 1
ch = 65 # The ACSII value of A is 65 

while(i <= n):
    j = 1
    while(j <= i):
        print(chr(ch), end=" ") # Convert ASCII value to character using chr() function and print
        ch = ch + 1
        j = j + 1
    print()
    i = i + 1


'''
Using the string 
A
BC
DEF
GHIJ
'''

n = 4
i = 1
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ch = 0
while(i <= n):
    j = 1
    while(j <= i):
        print(alphabets[ch], end=" ")
        ch = ch + 1 
        j = j + 1
    print()
    i = i + 1