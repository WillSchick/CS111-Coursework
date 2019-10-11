#Will Schick
#3/1/2018
#Gets input of temp from the user and determines whether or not the temp is freezing
print("--- " * 5) 

#variables & constants
isFreezing = bool

#userinput
temp = float(input("Input temperature (f): "))


#computation
if temp <= 32:
    isFreezing = True
else:
    isFreezing = False


#printing
if isFreezing:
    print("It's FREEZING!!")
else:
    print("It's above freezing.")
