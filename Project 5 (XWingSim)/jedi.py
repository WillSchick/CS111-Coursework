#Jedi.py
#Will Schick
#5/10/2018

#This module contains definition of the Jedi class.

#Jedi Class
# - Name: String
# - Lightsaber: Boolean


##Jedi class===============================================================================
class Jedi:
    ##Constructor----------------------------------------------------------------
    #returns none
    def __init__(self, name = "Luke Skywalker", lightsaber = False): #Takes input of name string, and lightsaber boolean
        self._name = name #Set name
        self._lightsaber = lightsaber #Set Lightsaber
        
    
    ##Accessors------------------------------------------------------------------
    #Returns name of the Jedi
    def getName(self): #Takes an input of self
        return self._name
    #Returns Lightsaber
    def hasLightsaber(self): #Takes an input of self
        return self._lightsaber
    
    
    ##Special Methods------------------------------------------------------------
    #Equals statement allows use of ==
    #Returns boolean
    def __eq__(self,secondJedi): #Takes input of a second jedi for comparison
        if (self._name == secondJedi.getName()): #If they have the same name
            if (self._lightsaber == secondJedi.hasLightsaber()): #Lightsaber equivalent test
                return True #Returns true if they're equal
        return False #Returns false if they're not equal
    
    #Not Equals statement allows use of !=
    #Returns boolean
    def __ne__(self,secondJedi): #Takes input of a second jedi for comparison
        if (self._name == secondJedi.getName()): #If they have the same name
            if (self._lightsaber == secondJedi.hasLightsaber()): #Lightsaber equivalent test
                return False #Returns false if they're equal
        return True #Returns true if they're not equal
            
        
    ##_repr_---------------------------------------------------------------------
    #Returns string containing a representation of the Jedi
    def __repr__(self): #Class representation for Jedi Class
        
        if self.hasLightsaber() == True: #String formatting for testing if has lightsaber
            hasLightsaber = " with a lightsaber."
        else:
            hasLightsaber = "."
        
        repr = "Jedi %s%s" % (self._name, hasLightsaber) #Repr
        
        return repr #Returns