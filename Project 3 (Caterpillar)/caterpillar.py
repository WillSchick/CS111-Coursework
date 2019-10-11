#caterpillar.py
#
#William Schick
#
#3/27/2018
#
#
from random import *


##Function plays the game from start to finish when called, doesn't return anything-------------------------------------
def playGame():
    
    welcome() #Draws a model of a complete caterpillar and welcomes the player
    
    #Loop init
    turn = 1
    antenna = 0
    head = 0
    body = 0
    leg = 0
    while (turn <= 30) and (isCaterpillarComplete(antenna,head,body,leg) == False):
        #Body
        if (turn == 30): 
            print("LAST TURN!!!") #Special text for the player's last turn
        else:
            print ("Turn ", turn,"---") #Text for the player's current turn
        
        #Roll for a body part
        roll = rollDie()
        print("You rolled a",roll)
        
        #Determine which body part the player got, and whether or not it can be applied
        if (roll == 1): #Antenna
            if useAntenna(antenna,head,body,leg) == True:
                antenna = antenna + 1 #Adds 1 to the antenna count if 
            
        elif (roll == 2): #Head
            if useHead(antenna,head,body,leg) == True:
                head = head + 1
            
        elif (roll == 3): #Body
            if useBody(antenna,head,body,leg) == True:
                body = body + 1
            
        elif (roll == 4) or (roll == 5): #Body
            if useLeg(antenna,head,body,leg) == True:
                leg = leg + 1
            
        
        elif (roll == 6):
            print ("Sorry! Lose a turn!")
        
        
        #Update
        print()
        input("Press [ENTER] to continue...")
        drawCaterpillar(antenna,head,body,leg)
        print()
        turn = turn + 1
    
    #Finishing the game
    if (isCaterpillarComplete(antenna,head,body,leg) == True): #If the player won
        print("Congratulations!!!! YOU WON!")
    else:
        print("Sorry! He's not quite complete... You lose.")
    
    return








##Takes in the number of caterpillar parts and prints a drawing-----------------------
def drawCaterpillar(antenna,head,body,leg):
    #Antenna------------------------------------
    if antenna == 0:
        print()
    elif antenna == 1:
        print("     \  ")
    elif antenna == 2:
        print("     \ /")
    
    #Head----------------------------------------
    if head == 0:
        print()
    elif head == 1:
        print("      O")
        
    #Body-----------------------------------------
    if body == 0:
        print("")
    elif body == 1:
        print("    ***") 
    elif body == 2:
        print("***=***")
        
    #Legs---------------------------------------
    if leg == 0:
        print("")
    elif leg == 1:
        print("      |") 
    elif leg == 2:
        print("     ||")
    elif leg == 3:
        print("    |||")
    elif leg == 4:
        print("  | |||")
    elif leg == 5:
        print(" || |||")
    elif leg == 6:
        print("||| |||")
    return

##Rolls and returns a number 1-6. ------------------------------------------------------
def rollDie():
    die = randint(1,6)
    return die

##Returns a True if the caterpillar has been fully assembled, False otherwise-----------
def isCaterpillarComplete(antenna,head,body,leg):
    if antenna == 2 and head == 1 and body == 2 and leg == 6:
        return True
    else:
        return False

##Returns True if the antenna is added to the caterpillar, returns false if it rejected----
def useAntenna(antenna, head, body, leg):
    if head == 0:
        print("Sorry! You can't add an antenna without having a head first!")
        return False
    elif head == 1:
        if antenna == 2:
            print("You already have two antennas! Sorry!")
            return False
        else:
            print("An antenna is added!")
            return True
                

##Returns True if the head is added to the caterpillar, returns false if it rejected----
def useHead(antenna, head, body, leg):
    if body == 0:
        print("Sorry! You can't add a head without having a body first!")
        return False
    elif body > 0:
        if head == 1:
            print("You already have a head! Sorry!")
            return False
        else:
            print("The head is added!")
            return True    
        

##Returns True if the body is added to the caterpillar, returns false if it rejected----
def useBody(antenna, head, body, leg):
    if body == 2:
        print("Sorry! You already have two body segments!")
        return False
    elif body < 2 :
        print("A body segment is added!")
        return True
         

##Returns True if the leg is added to the caterpillar, returns false if it rejected----
def useLeg(antenna, head, body, leg):
    if (body == 1 and leg == 3) or (body == 2 and leg == 6):
        print("Sorry! You are maxed out on legs!")
        return False
    elif body == 0:
        print("Sorry! You don't have a body to attach a leg to")
        return False
    else:
        print("A leg has been attached!")
        return True
    

##Initializes the game- (sort of a graphics function)----------------------------------
def welcome():
    print("********************************************")
    print("**** Welcome to the game of Caterpillar ****")
    print("********************************************")
    print()
    print("     \ /")
    print("      O")
    print("***=***")
    print("||| |||")
    print()
    
    
    