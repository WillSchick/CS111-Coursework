#emailAddress.py
#
#William Schick
#2/22/2018
#
#Prof. Givens
#
# Changes an name into a email username format
# William H Schick -> schickws

#Algorithm
#1: Assign a constant that will be appended to the end of the email: "@ezmail.org"
#2: User input for first name, middle, and last in seperate variables
#3: Assign variables to themselves but calling the lowercase method
#4: Print the last name, the first character of the first, and the first character of the middle name, and then append the "@ezmail.org" constant from step 1
#-----------------

#Clear console
print ("--- " * 5)

#Constant
tagLine = "@ezmail.org"

#User Input
first = input("What is your first name? :")
middle = input("What is your middle name? :")
last = input("What is your last name? :")

#Change variables to lower cases
first = first.lower()
middle = middle.lower()
last = last.lower()

#Print formatted
print("--- " *5)
print("Your email is:'%s%s%s%s'"%(last,first[0],middle[0],tagLine)) 



