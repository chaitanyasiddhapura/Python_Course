'''
1234554321
1234**4321
123****321
12******21
1********1

It's Combination of 3 pattern  
------------------------------------------------------
|   Pattern-1      |   Pattern-2   |    Pattern-3    | 
------------------------------------------------------             
|   12345          |               |        54321    |
|   1234           |      **       |         4321    |
|   123            |     ****      |          321    |
|   12             |    ******     |           21    |
|   1              |   ********    |            1    |
------------------------------------------------------

'''

n = 5
i = 1

while i <= n:
    # Logic for Print Number 
    CountNumber = n - i + 1 # Calculate how many number are print in each row 
    PrintNumber = 1
    while PrintNumber <= CountNumber: 
        print(PrintNumber,end=" ")
        PrintNumber = PrintNumber + 1
    

    # Logic for Print star
    star = (i - 1)*2 # Calculate how many star are print in each row 
    PrintStar = 1
    while(PrintStar <= star):
        print("*",end=" ")
        PrintStar = PrintStar + 1

    # Logic For a printing a reverse order of number like 54321 
    PrintNumber = PrintNumber - 1 
    while(PrintNumber > 0):
        print(PrintNumber,end=" ")
        PrintNumber = PrintNumber - 1
    
    print() # it's use for new line 
    i = i + 1




