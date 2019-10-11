# cylinder3.py
# 
# Created by: R. Necaise
#
# Modified by: Will Schick
# Date: 2/22/2018
#
# Given the dimensions of a cylinder, this program computes and 
# displays its surface area, circumference, and volume.
from math import pi

#Constants
PI = pi

# Initialize the cylinder properties.
print("--- --- " * 5)
height = float(input("Height: ")) #Default: 12
print("--- --- " * 5)
radius = float(input("Radius: ")) #Default 1.5

# Compute information related to the cylinder.
cir = (2 * PI * radius)
area = (2 * PI * radius * height)
volume = (PI * (radius**2) * height)

# Print the results.
print("--- Cylinder dimensions ---")
print("height = %.3f radius = %.3f" % (height, radius)) #Print the input from before to clarify (Rounded in case it was too crazy))
print("--- --- " * 5) #Divider
print("   area          = %10.3f" % (area)) #Print the area, rounded
print("   volume        = %10.3f" % (volume)) #Print the volume, rounded
print("   circumference = %10.3f" % (cir)) # Print the circumferance, rounded
