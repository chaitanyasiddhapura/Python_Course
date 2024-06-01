'''
Q1. Write a program to ask the user to enter name of their 3 favorite movie & store them in a list 
'''
movieName = []

# using the append() method 
movieName.append(input("Enter a favourite movie name 1:")) 
movieName.append(input("Enter a favourite movie name 2:")) 
movieName.append(input("Enter a favourite movie name 3:")) 

# print the list
print(movieName)

'''
Q2. Write a program to check if a list contains a palindrome of element. (hint: use copy() method) 
'''

list = [1, 2, 1]

listCopy = list.copy() # copy the list
listCopy.reverse() # reverse the list 
print(listCopy)

# check list it's palindrome or not 
if(list == listCopy):
    print("List is palindrome")
else:
    print("List is not palindrome")


