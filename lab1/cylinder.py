# cylinder.py
# 
# Name: William Schick
# Date: 2/15/2018
#
# Given the dimensions of a cylinder, this program computes its 
# surface area, circumference, and volume.

#Constants
PI = 3.1415926

#Declare
circumferance = float
surfaceArea = float
volume = float

#Clear the console
print("\n" * 25)

#Properties of the cylinder [INPUT]
height = 2.5
radius = 5

#Calculate properties of the cylinder
circumferance = (2 * PI * radius) #Calculate circumferance 2PiR
surfaceArea = (2 * PI * radius * height) #Calculate surface area 2PiRH
volume = (PI * (radius**2) * height) #Calculate volume Pi(R^2)H

# Print the results.
print ("---------Cylinder Dimensions---------")
print ("Height:", height, "   ...    Radius:",radius) #Declare the height and radius
print ("Circumferance:", circumferance) #Cirumference
print ("Surface Area:", surfaceArea) #Surface Area
print ("Volume:", volume) #Volume


