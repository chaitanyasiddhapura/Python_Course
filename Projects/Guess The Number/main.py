'''
Guess The Number 
'''

import random 

# Game start message
print("--- Start a Game ---")

# Genrete a random number using random module  
randomNumber = random.randint(1, 100)

# Loop until the user guesses the correct number
while True:
    UserChoice = input("Guess a number or Quit(Q): ") # User input for guessing the number

    # Exit the game 
    if(UserChoice == "Q"):
        break
    
    UserChoice = int(UserChoice)
    # Check if the user's guess is correct
    if(UserChoice == randomNumber): 
        print("Corret Your Guess are Win the game")
        break
    
    # Hint the user to guess a higher number
    elif(UserChoice < randomNumber):
        print("Your Number is smaller. Take a bigger number... ")
    
    # Hint the user to guess a lower number
    else:
        print("Your Number is larger. Take a smaller number...")

# Game over message 
print("--- Game Over ---") 