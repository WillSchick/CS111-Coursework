# moreFunctions.py
#
# Created by: R. Givens
# Modified by: Will Schick
#
# Module containing several functions that require if-statements and loops.
#Function 1: slope(x1,y1,x2,y2) - Calculates and returns the slope from an input of coordinates
#Function 2: telephone(letter) - Takes a letter and calculates a number based on the telephone phones
#Function 3: printSquare(num) - Takes an input number and prints all squares that preceed it
#Function 4: factorial(num) - Takes an input number and produces a factorial

##SLOPE---------------------------------------------------------------------------------
def slope(x1, y1, x2, y2):
    if (0 == x2 - x1):
        slop = "False"
    else:
        slop = (y2 - y1) / (x2 - x1)
        return slop


##TELEPHONE-----------------------------------------------------------------------------
def telephone(letter):

    letter = letter.upper()
    
    #computation
    if (letter in "ABC"):
        number = 2
    elif (letter in "DEF"):
        number = 3
    elif (letter in "GHI"):
        number = 4
    elif (letter in "JKL"):
        number = 5
    elif (letter in "MNO"):
        number = 6
    elif (letter in "PQRS"):
        number = 7
    elif (letter in "TUV"):
        number = 8
    elif (letter in "WXYZ"):
        number = 9    
    else:
        return -1
    
    return number

##PRINT SQUARES FUNCTION----------------------------------------------------------------
def printSquares(num):
    print("Squares up to", num, "---")
    
    #Loop setup
    x = 1
    square = 1
    while square < num :
        
        #Do stuff
        print(square)
        
        #Update
        x = x + 1
        square = x ** 2
    print("---"*5)
        

##FACTORIAL FUNCTION-----------------------------------------------------------------
def factorial(num):
    if num < 0:
        return 0
    else:
        #Loop set up
        count = 1
        factor = 1

        #Loop
        while count <= num:
    
            #Do stuff
            factor = factor * count #Multiply the current sum by the next number in the cycle
    
            #update
            count = count + 1
        
        return factor
