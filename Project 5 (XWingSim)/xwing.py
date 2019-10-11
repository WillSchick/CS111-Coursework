#xwing.py
#Will Schick
#5/10/2018

#This module contains definition of the Xwing class.

#Xwing Class
# - Pilot: Jedi Class
# - Speed: Float

from random import *
from jedi import Jedi


##Xwing Class=======================================================================
class Xwing:
    ##Constructor Method------------------------------------------
    #Constructs instance of Jedi class
    def __init__(self, jedi): #Takes an input of Jedi Class
        self._pilot = jedi #Sets pilot to an instance of Jedi class
        self._speed = randint(200,500) #Set random speed 200 - 500
      
        
    ##Accessor Methods--------------------------------------------
    #Returns string pilot name
    def getPilot(self): #Gets the name of our pilot
        return self._pilot.getName()
    
    #Returns boolean
    def isArmed(self): #Does the pilot have a lightsaber?
        return self._pilot.hasLightsaber()
    
    #Returns float of speed
    def getSpeed(self): #Gets the speed of the X-wing
        return self._speed
    
    
    ##Mutator Methods---------------------------------------------
    #Returns none
    def updateSpeed(self): #Updates the speed, adding 1-225 units
        self._speed = self._speed + randint(1,225)
        
        if self._speed > 500:
            self._speed = 500
            
        
    ##REPR-------------------------------------------------------
    #Returns string rep of X-wing instance
    def __repr__(self): #add our reprrrrrr
        
        rep = "X-wing with %s" % (self._pilot)
        
        return rep
        
        
        
  
        
               

        

        