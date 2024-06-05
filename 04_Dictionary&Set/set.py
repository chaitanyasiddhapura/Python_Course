'''
A set is a collection of unique, unordered items. 
Each item in a set must be unique, so repeated elements are stored only once.
Sets are mutable, meaning you can add or remove items from them.
However, the elements within a set must be immutable, so you can use numbers, strings, or tuples as elements, but not lists or dictionaries.
'''

sets = {1, 2, 3, 4, "Hello", "World"} # creating a set

print(sets) # print the set 
print(type(sets)) # print return type 
print(len(sets)) # find the length of set 


collection = set() #Creating a empty set 
print(type(collection)) # print the return type

'''
Set Methods
'''

collection.add(1) # add an element 
collection.add(2)
collection.add(2) # print only once 
collection.add(3)
print(collection)

collection.remove(2) # removes the element an
print(collection)


collection.clear() # empties the set
print(len(collection))


collection = {"Hello", "World","User"}

print(collection.pop()) # removes a random value 
print(collection.pop())
print(collection)


set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) # combines both set values & returns new 
print(set1.intersection(set2)) # combines common value & returns new 

