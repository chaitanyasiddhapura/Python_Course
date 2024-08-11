'''
Subtract the Product and Sum of Digits of an Integer

Notes: 

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15


Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        # Initialize Variable
        product = 1
        Sum = 0

        # Logic 
        while(n != 0): 
            Digit = n % 10  # Get the last digit of the number n
            product = product * Digit # Multiply the current digit with the product
            Sum = Sum + Digit # Add the current digit to the sum
            n = n // 10 # Remove the last digit from the number n

        Subtract = product - Sum # Calculate the difference between the product and the sum
        return Subtract
    
n = int(input("Enter a number: "))
Solution = Solution()
print(Solution.subtractProductAndSum(n))