'''
Q1. Store following word meaning in a python dictionary:
    table : "a piece of furniture", "list of facts & figures"
    cat: "a small animal"
'''

dictionary = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

print(dictionary)
print(type(dictionary ))


'''
Q2. Write a program to enter marks of 3 subject from the user and store them in a dictionary. 
Start with an empty dictionary & add one by one. Use subject name as key & mark as value.
'''

# 1st way: Adding marks to the dictionary one by one using direct assignment.
mark = {} # empty dictionary

# Add marks for each subject by taking input from the user and converting it to an integer
mark["phy"] = int(input("Enter phy mark: "))
mark["chem"] = int(input("Enter chem mark: "))
mark["Math"] = int(input("Enter a MATH mark: "))

print(mark) 

# 2nd way: Adding marks to the dictionary one by one using the update() method.
# Take input for each subject's marks and update the dictionary
x = int(input("Enter phy mark:"))
mark.update({"phy" : x})

x = int(input("Enter chem mark:"))
mark.update({"chem" : x})

x = int(input("Enter MATH mark:"))
mark.update({"Math" : x})

print(mark)
