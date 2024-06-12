'''
Q1. Print the element of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

# Numberlists = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for number in Numberlists:
#     print(number)
# print("End")


'''
Q2. Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

NumberTuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

NumberTOFind = int(input("Enter a number to be find in tuple: "))
index = 0
for number in NumberTuple:
    if(number == NumberTOFind):
        print("Number find in index position: ", index)
        break
    index = index + 1
print("END")  
