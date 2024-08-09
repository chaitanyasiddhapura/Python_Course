'''
Decimal TO Binary Conversion
'''

# User Input
n = int(input("Enter a number: "))

# Initialize 

BinaryNum = 0
i = 0
tempN = n # Store the original value of n


# Logic 

# If the number is negative, convert it to positive
if(n < 0):
    n = n * -1


# Loop to convert the number to binary
while(n != 0 ):
    bit = n & 1  # Get the least significant bit 
    BinaryNum =((10**i) * bit) + BinaryNum # Add the bit to the binary number at the correct position
    n = n >> 1  # Right shift by 1 is equivalent to integer division by 2
    i = i + 1 

# Check if the original number was negative
if(tempN < 0):
    print("Your Binary number is:","-",BinaryNum)
else:
    print("Your Binary number is:",BinaryNum)


'''
Updated Code
'''

n = int(input("Enter a number: "))

if n < 0:
    n = 2**16 + n

# print(n)

i = 0
ans = 0

while n > 0:
    last_bit = n & 1
    ans = (10**i) * last_bit + ans
    n = n >> 1
    i += 1
    # print(ans)

print(ans)
