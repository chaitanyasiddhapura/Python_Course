'''
Tuples is build-in data type that create immutable sequences of value  
'''

tuple1 = (1, 2, 3) # Syntax: tupleName = (value1, value2, .., valueN)
print(tuple1)
print(type(tuple1))

# Print tuple using the index 
print(tuple1[0])
print(tuple1[1])

# tuple1[0] = 12  # Tuples are immutable in Python, so we cannot assign a new value to an element.


# create a empty tuple
tuple2 = ()
print(tuple2)
print(type(tuple2))


tuple3 = (1)  # This is not a tuple. it's just an integer inside parentheses.
print(tuple3)
print(type(tuple3))

tuple4 = (1, ) # This is a tuple with a single element.
print(tuple4)
print(type(tuple4))

'''
create a slicing tuples 
'''
tuple5 = (1,3,5,6)
print(tuple5[ 1 : 3 ])


'''
Tuple Methods
'''
tuple6 = (64,565,25,34,87,64)

print(tuple6.index(34)) # return index of first occurrence 
print(tuple6.count(64)) # Counts total occurrence