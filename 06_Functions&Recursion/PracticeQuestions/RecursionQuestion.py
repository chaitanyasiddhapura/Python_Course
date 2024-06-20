'''
Q1. Write a recursive function to calculate the sum of first n natural numbers
'''

def sumN(n):
    if(n == 0):
        return 0
    return n + sumN(n - 1)
    
print(sumN(5))

'''
Write a recursive function to print all element in a list.
(Hint: use list & index as parameters)
'''

def printList(list, index = 0):
    if(index == len(list)):
        return
    print(list[index], end=" ")
    printList(list, index + 1)

list = [1, 2, 3, "Hello", "User"]
printList(list)
    