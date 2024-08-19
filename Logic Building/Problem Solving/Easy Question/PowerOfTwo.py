'''
Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
'''

def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    
    i = 0
    while (2**i <= n):
        if n == (2**i):
            return True
        i += 1
    
    return False

# Test cases
print(isPowerOfTwo(1))   # True
print(isPowerOfTwo(16))  # True
print(isPowerOfTwo(3))   # False
print(isPowerOfTwo(20))  # False

