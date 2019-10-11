#simulator.py
#Will Schick
#5/10/2018

def flightBattle(xwing1,xwing2,distance):
    
    #Display combatants
    print("********** Flight Battle Simulator **********")
    print(xwing1)
    print(xwing2)
    
    timeTilCombat = distance / (xwing1.getSpeed() + xwing2.getSpeed())
    print("Time until Xwings clash:", timeTilCombat, "minutes")
    
    #Pilot with lightsaber auto wins
    if (xwing1.hasLightsaber() and xwing2.hasLightsaber() == False):
        winner = xwing1
    elif (xwing2.hasLightsaber() and xwing1.hasLightsaber() == False):
        winner = xwing2
    else: #Determine a random winner if both or neither of them have lightsabers
        randWinner = randint(1,2)
        
        if randWinner == 1:
            winner = xwing1
        else:
            winner = xwing2
            
    print(winner.getPilot(),"wins.")
    
    