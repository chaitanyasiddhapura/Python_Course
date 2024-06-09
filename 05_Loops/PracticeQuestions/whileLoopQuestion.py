'''
Q1. print numbers from 1 to 100.
'''
count = 1
print("Print: 1 - 100 ")

while count <= 100:
    print(count)
    count = count + 1
print("END")



'''
Q2. Print numbers from 100 to 1.
'''
count = 100
print("Print: 100 - 1")
while count >= 1:
    print(count)
    count = count - 1
print("END")

'''
Q3. Print the multiplication table of a number n.
'''

UserInput = int(input("Enter Number: ")) # get the value from the user 
count = 1

while count <= 10: # until count vakue is 10
    table = UserInput * count # (UserInput = 10 * count = 2) = 20
    print(table)
    count += 1
print("Table Printed")

'''
Q4. Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0 # Initialize the index variable to 0, as list indices start from 0

while index < len(list): 
    print(list[index]) # Print the current element in the list
    index = index + 1 # Move to the next index
print("Printed")


'''
Q5. Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

tuples = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

valueTOfind = int(input("Enter the number to be find in tuples: "))
index = 0
# print(tuples[index])

while index < len(tuples): # Start a loop that runs as long as index is less than the length of the tuple
    if(valueTOfind == tuples[index] ): # Compare the input value with the current tuple value
        print("Value is find in position: ", index) # If they are equal, print the position of the value 
    index = index + 1

