'''
Dictionary are used to store data values in Key : value pairs
They are unordered mutable (changeable) & don't allow duplicate key
'''

# creating a Dictionary

info = {
    # key :  "value"
    "name" : "xyz",  # string value 
    "number" : 123456789, # integer value 
    "mark" : 89.65, # float value 
    "Boolean" : True, # boolean value   
    "list" : ["Hey","User", 123], # store List 
    "tuple" : ("Birth date","Adhar Number"), # store tuple 
    3432 : 32132 # key value may be number
}


print(info)
print(type(info)) # check the type of the variable 'info'
print(list(info)) # convert the dictionary keys into a list

info["name"] = "Chaitanya" # assign a new value to the key "name"
print(info)

'''
Creating Empty Dictionary
'''
emptyDictionary = {} 
print(emptyDictionary)

emptyDictionary["name"] = "User"
print(emptyDictionary)

'''
Nested Dictionary
'''

student = {
    "name" : "Chaitanya",
    "mark" : {
        "Math" : 89,
        "phy" : 98,
        "chem" : 80
    }

}

print(student) 
print(student["mark"]) # print the Nested Dictionary
print(student["mark"]["Math"]) # print the nested dictionary value

student["mark"]["Math"] = 90 # assign the value 
print(student["mark"]["Math"]) 

# convert Dictionary to list 
info = list(info) # use type cast
print(info)
print(type(info))

print(list(student))
print(list(student["mark"])) # to access the nested value in list


'''
Dictionary Methods
'''

print(student.keys()) # return all key
print(student.values()) # return all value 
print(student.items()) # return all (key, val) pairs as tuples 

# print(student["name"]) 
print(student.get("name1")) # return the key according to value 


student.update({"City" : "Remote"}) # inserts the specified item to the Dictionary
print(student)

    
