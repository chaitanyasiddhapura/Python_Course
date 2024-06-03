'''
Q1. Write a program to count the number of students with "A" grade in the following tuple
'''

GradeTuple = ("C","D","A","A","B","B","A") # Create a tuple 
print("The number of students with A grades is: ",GradeTuple.count("A")) # It counts how many times "A" appears in GradeTuple using the count() method.

'''
Q2. Store the above values in a list & sort them "A" to "D"
'''

Gradelist = ["C","D","A","A","B","B","A"] # Create a list  
print(sorted(GradeTuple)) # sort using sorted() method
