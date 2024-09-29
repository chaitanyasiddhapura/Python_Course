'''
A lambda function in Python is a small, anonymous function defined using the lambda keyword.
It can have any number of arguments but only one expression. 
The expression is evaluated and returned when the function is called. 
Lambda functions are often used for short, simple operations where defining a full function isn't necessary.
'''

from functools import reduce  # Importing reduce function from functools

# Lambda function to calculate power (x^x)
power = lambda x: x ** x
print(power(10))  # Output: 10^10 = 10000000000

'''
Lambda with filter function
'''
list1 = [1, 32, 456, 657, 234, 1234]

# Applying filter to get odd numbers from list1
filterList = filter(lambda x: (x % 2 != 0), list1)

# Converting the filter object to a list
filterList = list(filterList)

# Printing the filtered list of odd numbers
print(filterList)  # Output: [1, 657]

'''
Lambda with map function
'''
list2 = [1, 2, 3, 4, 5, 6]

# Using map to double each element in list2
doubledList = map(lambda x: x * 2, list2)

# Converting the map object to a list and printing it
print(list(doubledList))  # Output: [2, 4, 6, 8, 10, 12]

'''
Lambda with reduce function
'''
# Using reduce to calculate the sum of elements in list2
totalSum = reduce(lambda x, y: x + y, list2)

# Printing the total sum of elements
print(totalSum)  # Output: 21
