'''
Number of 1 Bits


Note:

Write a function that takes the binary representation of a positive integer and returns the number of 
set bits. it has (also known as the Hamming weight).

Example 1:
Input: n = 1
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
'''

def hammingWeight(n: int) -> int:
    # Initialize variable
    count = 0

    # Logic 
    while(n != 0):
        # Check if the last binary bit is 1
        if(n & 1):
            count = count + 1 # If yes, increase the count by 1
        n = n >> 1 # Shift the bits of n to the right by 1
    print(count)


n = 8
hammingWeight(n)
