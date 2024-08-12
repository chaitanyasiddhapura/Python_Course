'''
match Case Question


Designed a python code to break down an amount of money into the smallest number of notes possible using denominations of 100, 50, 20, and 1. 
'''

amount = int(input("Enter a amount: "))

i = 1
while(i <= 4):
    match(amount):
        case _ if(amount>100):
            count100 = amount//100
            amount = amount - (count100*100)
            print("Number of 100 RS note are required: ",count100)
        case _ if(amount>50):
            count50 = amount//50
            amount = amount - (count50*50)
            print("Number of 50 RS note are required: ",count50)
        case _ if(amount>20):
            count20 = amount//20
            amount = amount - (count20*20)
            print("Number of 20 RS note are required: ",count20)
        case _ if(amount>1):
            count1 = amount//1
            amount = amount - (count1*1)
            print("Number of 1 RS note are required: ",count1)
    i = i + 1


