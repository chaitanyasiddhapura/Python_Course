'''
Range function return a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number
Syntax: range(start?, stop, step?)
'''
# range(stop)
for i in range(5):  # Loop from 0 to 4
    print(i)

# range(start, stop)
for i in range(2,5): # Loop from 2 to 4
    print(i)

# range(start, stop, step)
for i in range(2, 10, 2): # Loop from 2 to 8, increasing by 2 each time
    print(i)


