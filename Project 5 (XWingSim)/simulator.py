#simulator.py
#Will Schick
#5/10/2018

#This modules contians flightBattle(), which has our X-wings and Jedi taking part in a simulated battle


from random import *

##flightBattle=====================================================================================================
#Returns the winner's name
def flightBattle(xwing1,xwing2,distance): #Takes an input of two xwing classes, and the distance between them
    
    #Display combatants------------------------------------------------------------
    print("********** Flight Battle Simulator **********")
    print(xwing1)
    print(xwing2)
    print()
    
    
    
    #Display time til clash--------------------------------------------------------
    timeTilCombat = distance / (xwing1.getSpeed() + xwing2.getSpeed())
    print("Time until X-wings clash: %.2f minutes." % (timeTilCombat))
    print()
    
    
    
    #Determine and display winner--------------------------------------------------
    #Pilot with lightsaber auto wins
    if (xwing1.isArmed() and xwing2.isArmed() == False):
        winner = xwing1.getPilot()
    elif (xwing2.isArmed() and xwing1.isArmed() == False):
        winner = xwing2.getPilot()
    else:
        #Determine a random winner if both or neither of them have lightsabers
        randWinner = randint(1,2)
        
        if randWinner == 1:
            winner = xwing1.getPilot()
        else:
            winner = xwing2.getPilot()
    
    #Print and return winner
    print(winner,"wins.")
    return winner
    