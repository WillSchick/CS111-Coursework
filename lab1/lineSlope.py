# lineSlope.py
#
# Created by: R. Necaise
# Modified by: William Schick
#
# Date: 2/15/2018
#
# This program computes the slope of a line given the end points of the
# line. The result is then displayed to the terminal.
#

#Clearing the console
print("\n" * 25)

# Initialize the end points.
startX = 5
startY = 12
endX = 30
endY = 17

# Compute the slope.
slope = (startY - endY) / (startX - endX) 
#Fixed indent

# Print the results.
print("Starting point: (", startX, ",", startY, ")") #Added Comma
print("Ending point: (", endX, ",", endY, ")")
print("Slope of the line =", slope) #Added quotation mark

