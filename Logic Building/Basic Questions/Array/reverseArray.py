'''
Reverse Array
''' 

def length(List: list) -> int:
    count = 0 
    for element in List:
        count = count + 1
    return count

def reversedArray(List: list):
    start = 0 
    end = length(List) - 1 
    i = 0
    while start <= end:
        temp = List[start]
        List[start] = List[end] 
        List[end] = temp
        start = start + 1
        end = end - 1
    
    print(List)

 
arr1 = [19, 2, 3, 56, 98, 0, 1]
arr2 = [30, 99, 78, 65, 45]


reversedArray(arr1)
reversedArray(arr2)