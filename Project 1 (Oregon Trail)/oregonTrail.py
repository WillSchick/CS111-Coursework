#Oregon Trail
#Will Schick
#3/6/2018

#imports
from random import *
from math import *

#Players will depart towards Oregon, picking a:
# - Profession
# - Season
# - Family Members
#
#Players will catch a number of animals along the way, and a number of party members will succumb to death.
#In the end they will make it to Oregon or perish along the way

print ("--- ")

#Variables used
profChoice = str #The choice the player makes regarding their profession
profession = str #The player's profession
money = int #The player's funds
familyMembers = int #The number of companions in the player's party
seasChoice = str #The choice the player makes regarding their starting season
season = str #The season the player leaves in
deaths = int #The ammount of deaths in the player's party
deathText = str #A specialized death text that prints depending on how many of the party dies along the way
animals = int #The ammount of animals the player has caught along the journey


#Constants
BANKER_START = 2000 #Banker starting cash
CARPENTER_START = 750 #Carpenter starting cash
FARMER_START = 500 #Farmer starting cash
PENALTY = 200 #Price for losing a party member
BONUS = 10 #Selling price of each animal


#Picking a player's profession!----------------------------------------------------------
print("Choose your profession:")
print("%5s %-20s" % ("1 -", "Banker,"))
print("%5s %-20s" % ("2 -", "Carpenter,"))
print("%5s %-20s" % ("3 -", "Farmer,"))
print()

profChoice = input("     : ") #Input player's choice

#Assign their profession based on their choice
if profChoice == "1":
    profession = "Banker"
    money = BANKER_START
elif profChoice == "2":
    profession = "Carpenter"
    money = CARPENTER_START
elif profChoice == "3":
    profession = "Farmer"
    money = FARMER_START
else:
    print("INVALID INPUT!!!")
    print()
    print (0/0)    
   
#Clarify 
print()
print("You are a", profession, "!")    
print ("--- "*5)


#Picking a player's number of family members---------------------------------------------
print ("Including yourself - how many members are in your company? (Maximum of 10)")
print()
familyMembers = int(input("    #: "))


#If the player has given an int between 1 and 10.
if familyMembers > 0 and familyMembers < 11:
    print()    
    print("You have", familyMembers - 1, "companion(s), for a party of", familyMembers)
else:
    print("INVALID INPUT!!!")
    print()
    print (0/0)


print ("--- "*5)


#Picking a player's departure season------------------------------------------------------
print("Choose your season of departure!:")
print("%5s %-20s" % ("1 -", "Spring / Summer,"))
print("%5s %-20s" % ("2 -", "Fall / Winter,"))
print()

seasChoice = input("     : ") #Input player's choice

#Assign their season based on their choice
if seasChoice == "1":
    season = "Spring / Summer"
elif seasChoice == "2":
    season = "Fall / Winter"
else:
    print("INVALID INPUT!!!")
    print()
    print (0/0)    
   
#Clarify 
print()
print("You are leaving in", season, "!")    
print ("--- "*5)

#Simulation-------------------------------------------------------------------------
#Spring and Summer Calculations-----------------------------------------------------
if season == "Spring / Summer":
    if profession == "Banker":
        deaths = randint(0, familyMembers // 2) #Banker Summer Deaths
        animals = randint(7,14) #Banker Summer Animals Caught
        
    elif profession == "Carpenter":
        deaths = randint(0, familyMembers // 3) #Carpenter Summer Deaths
        animals = familyMembers * 3 #Carpenter Summer Animals Caught
        
    elif profession == "Farmer":
        deaths = 0 #Farmer Summer Deaths 
        animals = familyMembers * 4 #Farmer Summer Animals Caught


#Fall and Winter Calculations-------------------------------------------------------
if season == "Fall / Winter":
    if profession == "Banker":
        deaths = randint(round(familyMembers * 0.5), familyMembers) #Banker Fall Deaths
        animals = 0  #Banker Fall Animals Caught
        
    elif profession == "Carpenter":
        deaths = randint(round(familyMembers * 0.333), round(familyMembers * 0.666)) #Carpenter Fall Deaths
        animals =  randint(familyMembers, familyMembers * 2) #Carpenter Fall Animals Caught
        
    elif profession == "Farmer":
        deaths = randint(0, round(familyMembers * 0.5)) #Farmer Fall Deaths
        animals =  randint(familyMembers, familyMembers * 3) #Farmer Fall Animals Caught
        

#FINAL STRETCH-------------------------(Printing Results)---------------------------------------------
print("--- Starting Conditions ---")
print(profession+ ", you've started the journey to Oregon!")
print("You have $", money, "in starting funds")
print("You have", familyMembers - 1, "companion(s), for a party of", familyMembers)
print("You are leaving in", season, "!")  
print()
print("Travelling...")
print()


#Deaths
if deaths == 0: #If nobody has died, display a special print to the player
    deathText = "Congratulations! None of the party has perished!"
elif deaths == 1: #If one person has died, display a special print to the player
    deathText = "Unfortunately-- one party member passed away on the long the journey."
else: #If multiple people have died, display a special print to the player
    deathText = "Oh no... "+ str(deaths)+ " members of the company have died along the perilous journey."

if deaths >= familyMembers: #If the entire party has died, trigger a gameover state
    print("Oh no!, the entire party has perished! You have died!")
    print("!----Game over----!")
else:
    #Win screen, print results
    print("You have arrived in Oregon!") 
    
    #Animals
    if animals == 0: #Displays a special text if the party didn't catch any animals
        print("The party didn't catch any animals on the way to Oregon.")
    elif animals == 1: #Displays a special text if the party only caught one animal
        print("The party caught just ONE animal on the way to Oregon.")
    else:
        print("The party caught", animals, "animals on the path to Oregon!")
    
    #Deaths
    print(deathText)

    #Funds
    money = (money + (animals * BONUS)) - (deaths * PENALTY)

    if money < 0:
        money = 0

    print("You have ended your journey with $"+ str(money), "in funds")
