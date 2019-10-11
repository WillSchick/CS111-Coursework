# roots.py
# 
# Created by: R. Necaise
#
# Modified by: Will Schick
# Date: 2/20/2018
#
# This program computes and displays the square and cube roots of 
# an integer value entered by the user.
print ("--- --- " * 5) #Clear the console

#import
from math import*

# Read the integer value from the user.
value = int(input("Enter an integer value: "))

# Compute the roots of the integer value entered by the user.
squareRoot = sqrt(value)
cubeRoot = pow(value, 1 / 3)

# Print the results.
print("x =", value)
print("--- --- " * 5)
print("square root(x) = %.2f" % (squareRoot))
print("cube root(x)   = %.2f" % (cubeRoot))


