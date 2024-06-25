'''
Q1. Creating a new file "Practice.txt" using python. Add the following data in it:
    Hi everyone
    we are learning File I/O
    using java
    I like programming in java
'''

with open('Practice.txt','w') as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using java\nI like programming in java\n")


'''
Q2. Write a program that replace all occurrnce of Java with python in above file.
'''

with open("Practice.txt",'r') as f:
    data = f.read()

UpdateData = data.replace('java', 'python')
print(UpdateData)

with open('practice.txt','w') as f:
    f.write(UpdateData)


'''
Q3. Search if the word "learning" exists in the file or not
'''
word = 'learning'
with open('practice.txt','r') as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

'''
Q4. Write a function to find in which line of the file does the word "learning" occur first.
print -1 if word not found.
'''

def findLineForWordIsOccur():
    word = 'dscfdfc'
    data = True
    LineNumber = 1 
    with open('practice.txt','r') as f:
        while data:
            data = f.readline()
            if(word in data):
                print(LineNumber)
                return 
            LineNumber = LineNumber + 1
    return -1     
    

print(findLineForWordIsOccur())

'''
Q5. From a file containing numbers separated by comma, print the count of even numbers.
'''
count = 0
with open('practice.txt','r') as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
 

