#xwing.py
#Will Schick
#5/10/2018

from random import *
from jedi import Jedi

class Xwing:
    ##Constructor Method------------------------------------------
    def __init__(self, jedi):
        self._pilot = jedi
        self._speed = randint(200,500)
      
        
    ##Accessor Methods--------------------------------------------
    def getPilot(self):
        return self._pilot.getName()
    
    def getPilot(self):
        return self._pilot.hasLightsaber()
    
    def getSpeed(self):
        return self._speed
    
    
    ##Mutator Methods---------------------------------------------
    def updateSpeed(self):
        self._speed = self._speed + randint(1,225)
        
        if self._speed > 500:
            self._speed = 500
            
        
    ##REPR-------------------------------------------------------
    def __repr__(self):
        
        rep = "Xwing with %s" % (self._pilot)
        
        return rep
        
        
        
  
        
               

        

        