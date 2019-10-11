#convertToCelcius.py

#Created: William Schick

#2/16/2018

#---

#Declare
farenheight = float
celsius = float

#Clear Console
print("-" * 15)
print("Begin")
print("-" * 15)

#User Input
farenheight = float(input("Input Farenheight: "))
print("-" * 15)


#Calculating Celsius from user input
celsius = round((5/9)*(farenheight - 32),2)


#Display Celsius
print("%12.3f degrees Farenheight" % (farenheight))
print("%12.3f degrees Celsius" % (celsius))
