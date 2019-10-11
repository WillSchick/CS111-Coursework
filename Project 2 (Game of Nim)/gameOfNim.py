#gameOfNim.py
#Will Schick
#3/22/2018

from math import *
from random import *

#Contents--------------------------------------------------------------------------
#Constants
#Welcome player
#Randomly choose amount of sticks
#Randomly choose who goes first
#Loop ( Gameplay )
#Player who drew the last stick loses



PLAYER = "You"
COMPUTER = "The computer"


#Welcome player---------------------------------------------------------------------
print()
print("**********************************")
print("*** WELCOME TO THE GAME OF NIM ***")
print("**********************************")

#Randomly choose amount of sticks--------------------------------------------------------
sticks = randint(25,50)
print("Whoever draws the last stick loses.")
print("You may draw multiple sticks at a time up to half the current number of sticks.")
print()

#Randomly choose who goes first----------------------------------------------------------
whoGoesFirst = randint(0,1)

if whoGoesFirst == 0:
    turn = PLAYER
else:
    turn = COMPUTER


#Loop ( Gameplay ) ---------------------------------------------------------------------
#Init
withdrawError = False
print(turn, "will go first")
while sticks > 1:
    withdrawError = False #If the player's turn has been reset due to error, set the error bool back to False
    #Body
    print()
    print("There are", sticks, "sticks left in the pile")
    
    if turn == PLAYER: #If it's the player's turn
        print()
        print("You can withdraw up to half the current total (",sticks//2,").")
        withdraw = int(input("Choose an amount of sticks to withraw from the stack: ")) #Input stick withdraw
        
        if withdraw <= 0 or withdraw > sticks//2: #If the withdraw is invalid
            print()
            print("---" * 5)
            print("Error - input a valid number of sticks!")
            print("---" * 5)
            withdrawError = True
        elif withdraw == 1: #Grammar- if the player withdraws only one stick.
            print("You withdraw just one stick.")
            sticks = sticks - withdraw
        else:
            print("You withdraw", withdraw, "sticks.")   
            sticks = sticks - withdraw
            
        
    else: #If it's the computer's turn
        #Computer takes sticks
        computerWithdraw = randint(1,sticks//2)
        sticks = sticks - computerWithdraw
        
        if (computerWithdraw == 1): #Grammar- if the computer withdraws only one stick.
            print("The computer withdraws just one stick.")
        else:
            print("The computer withdraws", computerWithdraw, "sticks.")
    
    #Update
    if turn == PLAYER and withdrawError == False:
        turn = COMPUTER
    else:
        turn = PLAYER
    


#Player who drew the last stick loses ---------------------------------------------------------------------
print()
print("There is only one stick left in the pile...")

if (turn == PLAYER):
    print("It is your turn...")
    print("You draw the last stick!")
    print("You lose!")
else:
    print()
    print("It is the computer's turn...")
    print()
    print("They draw the last stick!")
    print()
    print("CONGRATULATIONS!!!")
    