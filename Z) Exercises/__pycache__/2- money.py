#Money.py
#Will Schick
#2/14/2018

#Imports
from random import *
from math import *

#Clear the console
print ("--- " * 10)

#Declarations
PENNIES_TO_DOLLAR = 100

#Getting a random amount of pennies
pennies = randint(0,1000000) #Min amount 0, Max amount 1,000,000


#Sorting pennies into dollars and cents, and displaying values
print("Total Pennies: %d" % (pennies)) #Total amount of pennies before sorting
print("Value: $%d.%d" % ((pennies//PENNIES_TO_DOLLAR),(pennies%PENNIES_TO_DOLLAR))) #Dollar's worth of pennies







