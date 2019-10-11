#temp.py
#Will
#5/8/2018

#Module containing the class [Temperature]

class Temperature:
    ##CONSTRUCTOR METHOD----------------------------------------------
    def __init__(self):
        self._Celsius = 0
    
    ##ACCESSOR METHODS------------------------------------------------
    def getFahrenheit(self):
        return ((self._Celsius * (9/5)) + 32)
    
    def getCelsius(self):
        return self._Celsius
    
    ##MUTATOR METHODS------------------------------------------------
    def setFahrenheit(self, newFahrenheit):
        self._Celsius = (newFahrenheit - 32) * (5/9)
        
    def setCelsius(self, newCelsius):
        self._Celsius = newCelsius
    
    ##REPR METHOD----------------------------------------------------
    def __repr__(self):
        
        fahrenheit = ((self._Celsius * (9/5)) + 32)
        
        rep = "[ Fahrenheit = %.2f, Celsius = %.2f ]" % (fahrenheit, self._Celsius)
        return rep
        