#guess.py
#Will Schick
#3/13/2018
#This program will generate a random number from 1 to 30 and prompt the user 5 times to try and guess the number.
#The program will give hints as to whether their last guess was lower or higher than the correct number
from random import *
print("--- " * 5)


#The number!
number = randint(1,30)


#Loop setup
guess = 0
guessed = False
while guess < 5 and guessed == False:
    
    #Do stuff------------------------------------
    #Special prompt for the first guess
    if guess == 0:
        userGuess = int(input("Try and guess a number 1 - 30: "))
    else:
        userGuess = int(input("Guess again!: "))
    
    #Hint and win if statement
    if userGuess == number:
        print("Congratulations! You guessed it!")
        guessed = True
        
    elif userGuess > number: #If their guess is greater than the number
        print("Try lower")
        print()
        
    else: #If their guess is lower than the number
        print("Try higher")
        print()
    
    #update the loop--------------------------------------
    guess = guess + 1


#Print a special prompt if the user guessed right on the first try!
if guess == 1:
    print("Wow you got it on the first try too!!!")
else:
    print("You took", guess, "guesses!")



