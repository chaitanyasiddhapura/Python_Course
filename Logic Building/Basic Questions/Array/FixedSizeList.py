'''
List With fixed size 
'''   

n = 5
numbers =  [0] * n

print(numbers)

print("Enter a element in array: ")
for i in range(n):
    numbers[i] = int(input(""))

print(numbers)