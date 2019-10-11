#lists
#Will Schick
#4/11/2018
#
#
from random import *

shop = [
    "painting", 
    "gemstone", 
    "silverware", 
    "velvet", 
    "crown"
]

##Takes a random number
def randList(list,amount):
    i = 0
    randFromList = []
    
    while i < amount:
        #body
        randItem = randint(0, (len(list) - 1)) #Pick a random item from the given list
        randFromList.append(list[randItem]) #Add that item to the new list!
        
        #update
        i = i + 1
        
    return randFromList
    
pockets = randList(shop,15)
print(pockets)