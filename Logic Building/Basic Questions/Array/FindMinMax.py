'''
Find Min Max 
'''

def Maxi(List: list) -> int:
    Max = -2**32 # range of int 
    for element in List:
        if(element > Max):
            Max = element
            
    return Max

def Mini(List: list) -> int:
    Min = 2**30 # range of int 
    for element in List:
        if(element < Min):
            Min = element
            
    return Min

def printMinMax(List: list) -> None:
    print("Maximum:",Maxi(List))
    print("Minimum:",Mini(List))


num = [10, 23 , 2]
printMinMax(num)

