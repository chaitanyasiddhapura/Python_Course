'''
AAA
BBB
CCC
'''

n = 3
i = 1
ch = 65 # The ACSII value of A is 65 

# Outer loop for row
while(i <= n):
    j = 1 
    # Inner loop for column 
    while(j <= n):
        print(chr(ch), end=" ") # Convert ASCII value to character using chr() function and print 
        j = j + 1
    print()
    ch = ch + 1
    i = i + 1

print("*****")

'''
Using the string 
AAA
BBB
CCC
'''

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = 3
i = 1

while(i <= n):
    j = 1
    while(j <= n):
        ch = alphabets[i - 1]
        print(ch, end=" ")
        j = j + 1
    print()
    i = i + 1




