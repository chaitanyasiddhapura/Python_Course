'''
Python can be used to perform operations on a file.(Read & Write data)

Step : create a demo.txt file and write anything after that run this code 

Type of all file
    1) Text File: .txt, .docx, .log, etc.
    2) Binary File: .mp4, .mov, .png, .jpeg etc.
'''


# We have to open a file before reading or writing 

f = open("demo.txt","r") # open() use to open a file 

data = f.read() # read() are use to read the data from the file 

print(data)
print(type(data))

f.close() # close() are use to close the file 
