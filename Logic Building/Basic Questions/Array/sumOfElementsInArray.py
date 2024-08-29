'''
Sum of elements in array.
'''

# Find the length of list
def Length(List):
    count = 0 
    for i in List:
        count += 1
    print(count)

# Using While Loop
Numbers = [1,2,3,4,5]
Length(Numbers)
Sum = 0 
i = 0
while(i < len(Numbers)):
    Sum = Sum + Numbers[i] 
    i = i + 1

print(Sum)


# Using For loop
Numbers = [1,2,3,4,5]
Sum = 0 
for element in Numbers:
    Sum = Sum + element

print(Sum)