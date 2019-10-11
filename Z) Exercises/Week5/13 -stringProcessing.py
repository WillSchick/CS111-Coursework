#stringProcessing.py
#Will Schick
#8:37 - 4/9/2018
#
#

## RETURNS THE LOCATION OF THE FIRST DIGIT. -1 if no digits --------------------------------------------------
def firstDigit(string):
    i = 0
    
    while i < len(string):
        if string[i].isdigit():
            return i
    
        #Update
        i = i + 1
    
    
    return -1    
#-----------------------------


## Returns the location of the last digit. -1 if no digits --------------------------------------------------
def lastDigit(string):
    i = len(string) - 1
    
    while i >= 0:
        if string[i].isdigit(): #If the current index is a number
            return i #Return the index position
    
    return -1 #If the search has gone through the entire string and found no digit this will trigger
#----------------------------------
    








##COUNT THE UPPERCASE LETTERS IN A STRING ------------------------------------------
def countUppercase(string):
    
    uppercaseLetters = 0
    i = 0
    
    while i < len(string):
        
        if string[i].isupper():
            uppercaseLetters = uppercaseLetters + 1
        
        #update
        i = i + 1
    
    return uppercaseLetters



##EditCreditCard------------------------------------------------------------------
def editCreditCard(oldCard):
    #Setup
    i = 0
    newCard = ""
    
    #Loop through the indicies
    while i < len(oldCard):
        #grab the character
        char = oldCard[i]
        
        if char.isdigit():
            newCard = newCard + char
        