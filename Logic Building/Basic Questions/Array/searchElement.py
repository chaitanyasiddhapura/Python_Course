'''
Search Element in Array
'''

def length(List: list) -> int:
    count = 0 
    for element in List:
        count = count + 1
    return count


def search(List: list, key: int) -> bool:
    for element in List:
        if(element == key):
            return 1
    
    return 0

    '''
    # Using while loop
    i = 0 
    while(i < length(List)):
        if(List[i] == key):
            return 1
        i = i + 1
    return 0
    '''    
    

arr = [19, 2, 3, -5, 56, 98, -52, 0, 146, 1]
key = int(input("Enter element to be search:"))
result = search(arr, key)

if(result):
    print("Element is found")
else:
    print("Element is not found")

