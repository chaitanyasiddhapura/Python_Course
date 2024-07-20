'''
123
456
789
'''


# Define the number of rows and columns
rows = 3
cols = 3

# Initialize the starting number
number = 1

# Loop through each row
for i in range(rows):
    # Loop through each column in the current row
    for j in range(cols):
        # Print the current number without moving to a new line
        print(number, end="")
        # Increment the number for the next position
        number = number + 1
    # Move to the next line after finishing a row
    print()
