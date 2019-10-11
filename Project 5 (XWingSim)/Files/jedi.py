#Jedi.py
#Will Schick
#5/10/2018

#Jedi Class

class Jedi:
    ##Constructor----------------------------------------------------------------
    def __init__(self, name, lightsaber = False):
        self._name = name
        self._lightsaber = lightsaber
        
    
    ##Accessors------------------------------------------------------------------
    def getName(self): #Returns name
        return self._name
    
    def hasLightsaber(self): #Returns Lightsaber
        return self._lightsaber
    
    
    ##Special Methods------------------------------------------------------------
    #Equals statement allows use of ==
    def __eq__(self,secondJedi):
        if (self._name == secondJedi.getName()): #If they have the same name
            if (self._lightsaber == secondJedi.hasLightsaber()): #Lightsaber equivalent test
                return True #Returns true if they're equal
        else:
            return False #Returns false if they're not equal
    
    #Not Equals statement allows use of !=
    def __ne__(self,secondJedi):
        if (self._name == secondJedi.getName()): #If they have the same name
            if (self._lightsaber == secondJedi.hasLightsaber()): #Lightsaber equivalent test
                return False #Returns false if they're equal
        else:
            return True #Returns true if they're not equal
            
        
    ##_repr_---------------------------------------------------------------------
    def __repr__(self): #Class representation for Jedi Class
        
        if self.hasLightsaber() == True: #String formatting for testing if has lightsaber
            hasLightsaber = "has a lightsaber"
        else:
            hasLightsaber = "does not have a lightsaber"
        
        repr = "Jedi %s %s" % (self._name, hasLightsaber) #Repr
        
        return repr #Returns