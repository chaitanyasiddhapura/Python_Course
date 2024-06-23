# Read file using 'with'
with open('07_File&IO/demo.txt','r') as f:
    data = f.read()
    print(data)  
    

# With functiom automatically close the file

# Write file using 'with' 
with open("07_File&IO/demo.txt", 'w') as f:
    f.write("Hello")