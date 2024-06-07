'''
Q1. you are given a list of subject for student. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

    "python", "java", "C++","python", "javascript", 
    "java", "python", "java", "C++", "C"
'''

Totalsubject = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(Totalsubject)

# print(type(Totalsubject))

print("Total classroom required: ", len(Totalsubject))


'''
Q2. Figure out a way to store 9 & 9.0 as separate value in the set
(You can take help of build-in data type)
'''

# 1st way: Convert one of the numbers to a string.
# This way, "9.0" (string) and 9 (integer) are treated as different values.
numberSet = {"9.0", 9}
print(numberSet) # Output: {'9.0', 9}

# 2nd way: Use tuples to create distinct pairs for each value.
# Here, each number is paired with a type identifier, making them unique.
numberSet = {
    ("float", 9.0),
    ("int", 9)
}
print(numberSet)  # Output: {('int', 9), ('float', 9.0)}
