'''
Problem: Maximum Product of Three Numbers

You are given a list of integers. 
Your task is to write a Python function that returns the maximum product that can be obtained by multiplying exactly three different numbers from the list.

def maximum_product_of_three(arr: list) -> int:
    pass

'''
def maximum_product_of_three(arr: list) -> int:
    # Sort the array
    arr.sort()

    # Get the product of the three largest numbers
    product1 = arr[-1] * arr[-2] * arr[-3]
    
    # Get the product of the two smallest numbers and the largest number
    product2 = arr[0] * arr[1] * arr[-1]
    
    # Return the maximum of the two products
    return max(product1, product2)

arr1 = [1, 10, 2, 6, 5, 3]
print(maximum_product_of_three(arr1))  

arr2 = [-10, -10, 5, 2]
print(maximum_product_of_three(arr2))  

arr3 = [-1, -2, -3, -4]
print(maximum_product_of_three(arr3))  
