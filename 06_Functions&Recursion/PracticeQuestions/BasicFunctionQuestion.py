'''
Q1. Write a program to print the length of list. (list is the parameter)
'''
namelist = ["Chaitanya", "Krupal", "Utsav", "Krish", "Yash", "Madhav"]
numberlist = [1, 2, 3, 4, 5, 6, 7]
# 1 - way 
def printLength(lists):
    print(len(lists))

printLength(namelist)
printLength(numberlist)

# 2 - way 

def printLength(lists):
    count = 0
    for list in lists:
        count += 1
    print(count)

printLength(namelist)
printLength(numberlist)

'''
Q2. Write a program to print the elements of a list in a sigle line.(List is the parameter)
'''
# 1- way 
numberlist = [1, 2, 3, 4, 5, 6, 7]
print(numberlist)

# 2 - way 
def printlist(list):
    print(list)

print(namelist)
print(numberlist)

# 3 - way

def printlist(lists):
    for list in lists:
        print(list, end=" ")

printlist(namelist)
print()
print(numberlist)


'''
Q3. Write a program to find the factorial of n. (n is the parameter) 
''' 


def factorial(n):
    i = 1
    facto = 1
    while i <= n: 
        facto *= i  
        i = i + 1
    print(facto)

factorial(5)



'''
Q4. Write a program to convert USD to INR.
'''

def USDtoINR(USD):
    INR = USD * 80 
    print("INR:",INR)

USDtoINR(1000)


'''
Q5. Write a function for find number is even or odd 
'''

def EvenOROdd(value):
    if(value % 2 == 0):
        print("Even")
    else:
        print("Odd")


EvenOROdd(155)
EvenOROdd(198)
EvenOROdd(10)
EvenOROdd(11)


