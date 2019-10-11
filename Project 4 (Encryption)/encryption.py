# encryption.py
# Created by: R. Givens
# Modified by: William Schick
# Description: Module for creating and reading encrypted files

## letter constant, also required for tester, DO NOT CHANGE
# use indices of LETTERS for encryption/decryption
LETTERS = "abcdefghijklmnopqrstuvwxyz"


##---------------------------------------------------------------------------------------------
def encryptDigit(digit, shift): #Takes a digit, and the amount to shift it by
    return (digit + shift) % 10 #runs the digit through the encryption formula and returns it


##---------------------------------------------------------------------------------------------
def decryptDigit(digit, shift): #Takes an encrypted digit and the cypher shift
    return (digit - shift)%10 #Runs the digit through the decryption formula and returns it


##---------------------------------------------------------------------------------------------
def encryptChar(char, shift): #Takes a character and the amount to shift it by
    
    #For this loop, in the future you can use: LETTERS.index(char)
    for i in range(0,len(LETTERS)): #Shift through letters 
        if (char.lower() == LETTERS[i]): #until we find an index matching char
            index = i #Set our new index variable to the index of char
    
    encryptedIndex = (index + shift)%(len(LETTERS)) #Run the index through encryption
    
    if (char.upper() == char): #If char was originally uppercase
        return LETTERS[encryptedIndex].upper() #Return an uppercase version of the encrypted
    else:
        return LETTERS[encryptedIndex] #Return the lowercase


##---------------------------------------------------------------------------------------------
def decryptChar(char, shift): #Takes an encrypted char and the cypher shift
    index = LETTERS.index(char.lower()) #Find the index of char as found in LETTERS
    decryptedIndex = (index - shift)%(len(LETTERS)) #Run the index through decryption
    
    if (char.upper() == char): #If char was originally uppercase
        return LETTERS[decryptedIndex].upper() #Return an uppercase version of the encrypted
    else:
        return LETTERS[decryptedIndex] #Return the lowercase    


##---------------------------------------------------------------------------------------------
def convertString(string, shift, encrypt): #Takes a string, the cypher shift, and a boolean to determine whether to encrypt or decrypt
    
    newString = "" #Establish a new string
    
    #ENCRYPTION
    if encrypt == True: 
        for i in string: #Loop through the string
            if i.lower() in LETTERS: #If the character is a letter 
                newString = newString + encryptChar(i,shift) #Add decrypted letters to a new string
            elif i.isdigit():
                newString = newString + str(encryptDigit(int(i),shift)) #Add decrypted digit to a new string
            else:
                newString = newString + i
    
    #DECRYPTION
    elif encrypt == False:
        for i in string: #Loop through the string
            if i.lower() in LETTERS: #If the character is a letter
                newString = newString + decryptChar(i,shift) #Add decrypted letters to a new string
            elif i.isdigit():
                newString = newString + str(decryptDigit(int(i),shift)) #Add decrypted digit to a new string
            else:
                newString = newString + i
            
    return newString #Returns the new (encrypted / decrypted) string


##---------------------------------------------------------------------------------------------
def convertFile(inputName, outputName, shift, encrypt): #Takes the input file name for reading, output file name for writing, cypher shift, and whether or not to encrypt or decrypt the input file
    
    rFile = open(inputName,"r") #Establish the read file
    wFile = open(outputName,"w") #Establish the write file
    
    line = rFile.readline() #Read the first line (this will also be our update later)
    
    while line != "": #While there are lines left to read
        
        wFile.write(convertString(line,shift,encrypt)) #Convert a line, and write the conversion to the output file
        #wFile.write("\n")
        
        #update
        line = rFile.readline() #Our update, same as our init from above. Moves to a new line for reading.
        
    
    
    rFile.close() #close the read file
    wFile.close() #close the write file
    return #return void
    
    
