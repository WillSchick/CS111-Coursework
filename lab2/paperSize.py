#paperSize.py

#Will Schick

#2/20/2018

#This program takes the width and height of a paper from the user - and calculates perimeter and diagonal length and outputs it to the console
#-------------------
print ("--- --- " * 5)


#import
from math import*


#constants


#variables / input
width = float(input("Width of your paper: ")) #8
height = float(input("Height of your paper: ")) #11.5


#calculations
perimeter = 2 * (width + height)
diagonal = sqrt((width ** 2) + (height ** 2))

#print
print("--- " * 5)
print("%20s: %10.2f x %5.2f" % ("Paper Dimensions", width, height))
print("%20s: %10.2f" % ("Perimeter", perimeter))
print("%20s: %10.2f" % ("Diagonal Length", diagonal))
print("---" * 5)

