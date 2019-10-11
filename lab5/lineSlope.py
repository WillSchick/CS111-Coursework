# lineSlope.py
#
# created by: R. Necaise
# modified by: Will Schick 
# last modified: 3/1/2018 @ (1:22 PM)
#
# This program computes the slope of a line from discrete end points 
# extracted from the user. 

# Read the end-points from the user.
print("Enter the coordinates for the starting point.")
startX = int(input("x-coord: "))
startY = int(input("y-coord: "))

print("Enter the coordinates for the ending point.")
endX = int(input("x-coord: "))
endY = int(input("y-coord: "))

#Print the input
print("--- " * 5)
print("Starting point: (%d, %d)" % (startX, startY))
print("Ending point:   (%d, %d)" % (endX, endY))
print("--- " * 5)

# Make sure we can compute the slope of the line.
if startX == endX: #Forgot another "="
    print("Error: the slope can not be computed.")    
else: #Forgot a ":" 
    slope = (startY - endY) / (startX - endX)
    print("Slope of the line = %.2f" % slope) #Print the slope
