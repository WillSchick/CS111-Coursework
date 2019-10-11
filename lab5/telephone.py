#Will Schick
#3/1/2018 (1:42 PM)
#This program takes a character from a user and converts it into its corresponding number on a telephone
print ("--- " *5)


#userInput
char = input("Enter a letter: ").upper()
print ("Your letter: "+char)


#variables
telNumber = int
error = bool


#computation
if (char in "ABC"):
    telNumber = 2
elif (char in "DEF"):
    telNumber = 3
elif (char in "GHI"):
    telNumber = 4
elif (char in "JKL"):
    telNumber = 5
elif (char in "MNO"):
    telNumber = 6
elif (char in "PQRS"):
    telNumber = 7
elif (char in "TUV"):
    telNumber = 8
elif (char in "WXYZ"):
    telNumber = 9    
else:
    error = True
    

#printing
if error == True:
    print("Your input was invalid!!!")
else:
    print(telNumber)

