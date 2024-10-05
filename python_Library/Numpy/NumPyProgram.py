'''
NumPy is a Python library used for numerical computing. 
It helps us work with arrays (collections of numbers or data) easily and efficiently.

Before using NumPy, you need to install it. Run the following command in your terminal or command prompt:
pip install numpy

'''


# Importing NumPy
import numpy as np 

# An array is like a list, but it allows us to perform operations on large amounts of data efficiently.

'''
    Creating Arrays
'''

# 1D Array (simple list of numbers):
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2D Array (like a matrix):
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Type cast list into NumPy array
list1 = [1,2,3,4]
numPyArray1 = np.array(list1)

print(numPyArray1)
print(type(numPyArray1))

numPyArray2 = np.array([[1,2,3,4],[5,6,7,8]])
print(numPyArray2)

'''
    Basic Array Operations
'''

# Array of zeros: Creates an array filled with zeros.
n1 = np.zeros((2,3))
print(n1)
print(type(n1))

n2 = np.zeros((5,5))
print(n2)

# Array of ones: Creates an array filled with ones.
ones = np.ones((3, 3))
print(ones)

# Fills with a specific value: Creates an array filled with a specified value.
n3 = np.full((3,2),5)
print(n3)


# Range of numbers: Creates an array with a sequence of numbers.
n4 = np.arange(10, 20)
print(n4)

n5 = np.arange(10, 100, 5)
print(n5)


# Random numbers: Creates an array with random values.
n6 = np.random.randint(100, 200, 10)
print(n6)

n7 = np.array([[1,2,3,4],[5,6,7,8]])
print(n7)

# shape is use to check the dimensions of an array or change its structure.
n7.shape = (8, 1)
print(n7) 