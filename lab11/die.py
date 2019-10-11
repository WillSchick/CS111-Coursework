# die.py
#
# Created by: R. Necaise
#
# Defines a class that represents a 6-sided die with face values between 1
# and 6. Rolling of the die is simulated using the random number generator.

from random import randint 

class Die :
   # Initializes the face value to 1.
  def __init__(self) :
    self._faceValue = 1
    
   # Returns the face value of the die.
  def getValue(self) :
    return self._faceValue
    
   # Simulates the rolling of the die. The face value is returned.
  def roll(self) :
    newValue = randint(1, 6)
    self._faceValue = newValue
    return newValue
  
