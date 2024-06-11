'''
A for loop is generally used for sequential traversal, such as for traversing lists, strings, tuples, etc.
'''

# Code 1: List of numbers
nums = [1, 2, 3, 4, 5]

for value in nums: # Iterate over each number in the nums list
    print(value) # Print the current number

print("END") # This line executes after the for loop ends


# Code 2: List of names
namelist = ["Chaitanya", "Rishi", "Krish","Yash","Krupal"]

for name in namelist: # Iterate over each name in the namelist
    print(name) # Print the current name

# This block executes after the for loop completes normally
else: 
    print("End") # Indicate the end of the loop


# Code 3: Single name string
name = "Chaitanya"

for char in name: # Iterate over each character in the name string
    print(char) # Print the current character
print("END")