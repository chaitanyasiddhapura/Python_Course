# How to use of "if", "elif", "else" 

# Q1 Check you are eligible for vote

age = int(input("Enter your age: "))

if(age >= 18):
    print("Congratulation! You are Eligible for a vote")
else:
    print("Sorry! You are Not Eligible for a vote ")

# Q2 Check your grade

mark = int(input("Enter your marks: "))

if( mark >= 90 ):
    print("Grade - A")
elif( mark >= 70):
    print(" Grade - B ")
elif( mark >= 50):
    print(" Grade - C ")
elif( mark >= 30):
    print(" Grade - D ")
else:
    print("Sorry! You are fail.")


# Here, the example of sigle if/ ternary operator
# Syntax 1: <var> = <var1> if <condition> else<var2>
food1 = input("Food: ")
eat = "Yes" if food1 == "Cake" else "no"
print(eat)

# Syntax 2: <statement1> if <condition> else<statement2>
food2 = input("Food: ")
print("Sweet") if food2 == "Cake" or food2 =="jalebi" else print("Not Sweet")


# Here, the example of Clever if/ternary operator
# Syntax: <var> = (false_val, true_val)[<condition>]

# Example 1:
age1 = int(input("Age: "))
vote = ("yes", "no") [age1 < 18]
print(vote)

# Example 2:
sal = float(input("Salary: "))
tax = sal*(0.0, 0.1) [sal > 50000]
print(tax)
