#snakeEyes.py
#Will Schick
#5/8/2018

#Driver module that uses the Die class to repeatedly roll two dice until snake eyes are rolled.

#Imports
from die import Die


def main():
    
    #Declare our dice
    die1 = Die()
    die2 = Die()
    
    #init (Randomizes our face values)
    die1.roll()
    die2.roll()
    
    #While we don't have snake eyes
    while (die1.getValue() + die2.getValue()) != 2:
        
        #Update (Reroll our die)
        die1.roll()
        die2.roll()

        #Print the roll of our die, this comes after update so that it will print 1,1 at the end
        print(die1.getValue() , die2.getValue())         
        
    #Since our while statement doesn't stop until snake eyes, we're good
    print("Snake Eyes!!!!")


main()





