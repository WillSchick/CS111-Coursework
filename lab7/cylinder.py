# cylinder.py
#
# Created by: R. Necaise
# Modified by: Will Schick
#
# Illustrates the use of functions by computing the volume and surface
# area of a cylinder.

from math import pi

def main() :
  # Obtain the size of cylinder.
  print("Enter the size of the cylinder.")
  radius = float(input("radius: "))
  height = float(input("height: "))
  
  # Compute the data.
  volume = cylinderVolume(radius, height)
  area = cylinderArea(radius, height)
  
  # Print the results.
  print("The volume of the cylinder is %.2f" % volume)
  print("The total surface area of the cylinder is %.2f" % area)

# Add the missing functions below this line.

##CALCULATES CYLINDER VOLUME -------------------------------------------------------
def cylinderVolume(radius, height):
  volume = 3.1415926 * (radius**2) * height  
  return volume

##
def cylinderArea(radius, height):
  area = 2 * 3.1415926 * (radius * (radius + height))  
  return area



main()
