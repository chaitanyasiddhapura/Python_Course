'''
 String is the data type that store a sequence of characters 
'''

str1 = "Hey, user."
str2 = "How are you"

''' 
Basic operation 
'''

# 1. Concatenation 
str3 = str1 + str2 
print(str3)

print(str1 + str2)

print(str1 + " " + str2)


# 2. Find Length of str using len() function 
print(len(str1))

# 3. Indexing
ch = str1[1]
print(ch)

# 4. Slicing 
'''
Accessing parts of a string 
Syntax: str[Staring_index : Ending_index ]

String = Hey, user.
[index] = data,
[0] = H, [1] = e, [2] = y , [3] = ,, [4] = " ", [5] = u, [6] = s, [7] = e, [8] = r, [9] = .

Note: The slice includes characters from the start index up to, but not including, the end index. 
For example, using str1[5:8] will include characters at indexes 5, 6, and 7, but not 8. 
slicing =str1[5 : 8] this line of code print "use" only but need to print "user"  it includes characters at index 5, 6, and 7, but not 8. 
To print "user", you need to include characters from index 5 to 8. Therefore, the correct slice should be str1[5:9].
'''
slicing = str1[5 : 9] 
print(slicing)

slicing = str1[0: ] # it start [0 : end_index]
print(slicing)

slicing = str1[ :10] #  [0 : 10] position
print(slicing)

'''
 Negative index slicing
Example..,
Hey
[-3] = H, [-2] = e, [-1] = y 
'''
str3 = "Hey"
nagativeSlicing = str3[-3 : -1]
print("Nagative Slicing:",nagativeSlicing)

# Some other string function 

str4 = "i am a coder."

print(str4.endswith("er.")) # returns true if string end with substring 
print(str4.capitalize()) # Capitalize 1st char
print(str4.replace("i am ","I'm ")) # replace all occurrences of old
print(str4.find("coder")) # return 1st index of 1st occurrer
print(str4.count("coder")) # Counts the occurrence of substr 


