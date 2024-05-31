'''
Lists is build-in data type that store set of values
'''

mark = [55,56,98,68,89] # Syntax: list_name = [value1, value2, ..., valueN]
print(mark)
 
print(type(mark)) # Print the type 

print(mark[0],mark[1]) # Accessing the elements at index 0 and index 1 

# List is mutable 
name = ["Chaitanya","Krupal", "Utsav", "Krutik"]
print("Before value change: ", name)
name[1] = "Krish"
print("After value change: ", name)

'''
List Slicing it's similar to string slicing
'''

# Synatx: listName[Starting_idx : ending_idx]
mark = [55,56,98,68,89]
print(mark[1 : 4]) # is [56,98,68]
print(mark[ : 4]) # is same as mark[0 : 4]
print(mark[1 : ]) # is same as mark[1 : len(mark)]
print(mark[-3 : -1]) # is [33,95]

'''
List Methods
'''
list = [2,1,3]

list.append(4) # adds one element at the end
print(list)

list.sort() # sorts in ascending order 
print(list)

list.sort(reverse = True) # sorts in descending order 
print(list)

list.reverse() # reverse list 
print(list)

list.insert(1,12) #insert element at index
print(list)

list.remove(1) # Removes first occurrence of element
print(list)

list.pop(3) # removes element at idx
print(list)






