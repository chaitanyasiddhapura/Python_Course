'''
Break used to terminate the loop when encountered.
'''
# Initialize
i = 0 

# Logic 
while i <= 5:
    print(i) # Print the current value of i
    if(i == 3):  # Check if the value of i is 3
        break # If i is 3, exit the loop immediately
    i = i + 1 


'''
Continue terminate execution in the current iteration & continues execution of the loop with the next iteration
'''
# Initialize
i = 1 

# Logic
while i <= 10 :
    if(i % 2 !=  0):  # Check if i is an odd number (i % 2 != 0)
        i = i + 1  # If i is odd, increment it by 1
        continue # Skip the rest of the current loop and start the next iteration
    print("Even Number: ",i) # If i is even, print Even Number 
    i = i + 1


