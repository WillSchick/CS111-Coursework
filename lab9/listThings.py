#listThings.py
#Will Schick
#4/17/2018


##Returns the product of all the elements in the list or 1 if the list is empty.
def product(values):
    i = 0
    product = 1
    
    #Loop through the indicies and produce a product
    while i < len(values):
        #body
        product = product * values[i]
        
        #Update
        i = i + 1
        
    return product


##Returns the number of odd numbers in the list. Does not alter the list.
def countOdds(values):
    #setup
    i = 0
    oddCount = 0
    
    #Loop through the indicies and count the amount of odds
    while i < len(values):
        #Body
        if (values[i] % 2) == 1: #If the remainder is 1, AKA if it's odd
            oddCount = oddCount + 1 #Add to the odd count
            
        #Update
        i = i + 1
    
    #return
    return oddCount


##Returns a new list containing the squares of each value in the original list.
def squares(values):
    #setup
    i = 0
    newList = [] #Create a new list
    
    #Loop through the indicies and append their squares to the new list
    while i < len(values):
        #Body
        newList.append(values[i]*values[i])
        #Update
        i = i + 1
    
    #return
    return newList


##Computes and returns the alternating sum of the integer elements in the list.
def computeAltSum(values):
    i = 0
    altSum = 0
    subtracting = False
    
    #Loop through the indicies, alternating between addition and subtraction to a sum
    while i < len(values):
        #Body
        if subtracting == True:
            altSum = altSum - values[i]
            subtracting = False
        else:
            altSum = altSum + values[i]
            subtracting = True
            
        #update
        i = i + 1
        
    #Return
    return altSum


##Alters the list by replacing each negative value in the list to 0. 
def replaceNegatives(values):
    i = 0 
    
    #Loop through the indicies, replacing any negative numbers with zeros
    while i < len(values):
        #body
        if values[i] < 0:
            values[i] = 0
        
        #update
        i = i + 1
    
    return


##Shifts all the elements one position to the right. Moves the last element to the first position.
def shiftRight(values):
    #setup
    i = (len(values) - 1)
    if len(values) > 1:
        lastValueHolder = values[-1] #Holds on to the last value so we can replace the first later
    
    while i >= 0:
        #Body
        if i > 0: #If I is still looping through
            values[i] = values[i-1]
        else: #If I has reached the end
            values[0] = lastValueHolder #Replace the first index with the last we saved earlier
        
        #update
        i = i - 1

    #return
    return
