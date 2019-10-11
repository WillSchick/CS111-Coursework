#Will
#5/4/2018
#
# This program will create a Pet class.

##Class called Pet
#   Pets have a name, a species, and an age
class Pet: #<--A
    
    ##Constructor method
    #Assign name, species, age
    #Create an instance of the class pet
    def __init__(self, aName = "Zoop", aSpecies = "AlienDog", anAge = 5):
        # create and assign the instance variables (initialization)
        self._name = aName
        self._species = aSpecies
        self._age = anAge
        
        
    ## getter for the instance variable_name
    def getName(self):
        return self._name        
        
    ## getter for the instance variable_species
    # return the value of the instance variable
    def getSpecies(self):
        return self._species
    
    ## getter for the instance variable_age
    def getAge(self):
        return self._age
    
    
    ## Setter for instance variable name
    #Receives value, replaces value in instance variable
    def setName(self,aName):
        self._name = aName
        return
    
    ## Setter for instance variable name
    #Receives value, replaces value in instance variable
    def setSpecies(self,aSpecies):
        self._species = aSpecies
        
    ## Setter for instance variable name
    #Receives value, replaces value in instance variable
    def setSpecies(self,anAge):
        self._anAge = anAge   
        
    ## Birthday method
    # increase the age of the pet by 1 year
    def birthday(self):
        self.age = self._age + 1
        
    ## isCat method
    # return true if the species is a cat, false otherwise
    def isCat(self):
        if self._species.lower() == "cat":
            return True
        return False
    
    ## humanYears method
    # return the "human age" of the pet give its current age
    def humanYears(self):
        return 5 * self._age
    
    ## string representation
    # return a string containing the information for the pet
    def __repr__(self):
        
        if self._species[o].lower() in "aeiou":
            determiner = "an"
        else:
            determiner = "a"
        
        rep = self._name + "is" + determiner + self._species + str(self._age)


   
    
    