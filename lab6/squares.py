# squares.py
#
# Created by: R. Necaise
# Modified by: Will Schick
#
# This program prints all squares less than n where the value of n is
# entered by the user.

# Read the value from the user.
print("Print all squares less than n.")
n = int(input("Enter the value of n: "))

#Loop setup
x = 1
square = 1
while square < n :
  
  #Do stuff
  print(square)
  
  #Update
  x = x + 1
  square = x ** 2
  


