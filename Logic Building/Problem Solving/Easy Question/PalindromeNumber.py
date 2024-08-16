'''
Palindrome Number


Note:
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


'''
If you are not using the class  
'''

def reverseNumber(n: int) -> int:
    reverseAns = 0
    while(n > 0):
        singleDigit = n % 10
        reverseAns = (reverseAns * 10) + singleDigit
        n = n // 10
    return reverseAns

def isPalindrome(x: int) -> bool:
    if(x == reverseNumber(x)):
        return True
    else:
        return False
    
x = 121
result = isPalindrome(x)
print(result)

'''
If you are using the class   
'''

class PalidromeNum:

    def reverseNumber(self, n: int) -> int:
        reverseAns = 0
        while(n > 0):
            singleDigit = n % 10
            reverseAns = (reverseAns * 10) + singleDigit
            n = n // 10
        return reverseAns

    def isPalindrome(self, x: int) -> bool:
        if(x == self.reverseNumber(x)):
            return True
        else:
            return False
        
P1 = PalidromeNum()
x = 121
result = P1.isPalindrome(x)
print(result)

