'''
Swap Atternate

Example:

    Input - 1: 
    arr = [10, 20, 30, 40, 50, 60]
    Output:
    arr = [20, 10, 40, 30, 60, 50]

    Input - 2: 
    arr = [10, 20, 30, 40, 50]
    Output:
    arr = [20, 10, 40, 30, 50]

'''
def swapAtternate(arr: list):
    i = 0
    while i < len(arr):
        if(i+1 < len(arr)):
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
        i = i + 2
    print(arr)


arr1 = [10, 20, 30, 40, 50, 60]
arr2 = [10, 20, 30, 40, 50]
arr3 = []
arr4 = [1]
arr5 = [1, 2]
 
swapAtternate(arr1)
swapAtternate(arr2)
swapAtternate(arr3)
swapAtternate(arr4)
swapAtternate(arr5)