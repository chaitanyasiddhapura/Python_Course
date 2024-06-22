'''
Writing to a file 

mode: 
    'r' = Open for reading (default)
    'w' = Write mode overright mode 
    'a' = append add at the end 
    'x' = create a new file and open it for writing
    'b' = binary mode 
    't' = text mode (default)
    '+' = open a disk file for updating (reading and writing)
'''

# Write mode  
f = open('demo.txt','w')
f.write("Hello, I'm user.")
f.close()


# Append mode
f = open('demo.txt','a')
f.write("I am learning a python.")
f.close()


'''
Some other mode

    'r+' = read + overwrite (ptr point to the start) - no truncate
    'w+' = read + overwrite - truncate
    'a+' = read + append (ptr point to the end) - no truncate

'''