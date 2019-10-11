# stringThings.py
#
# Created by: R. Givens
# Modified by: Will Schick on 4/10/2018 @ 1:41 PM
#
# Module containing several functions that process strings.

##Loop through the indices and count the amount of digits
def countDigits(string): 
     i = 0
     digitCount = 0
     
     while i <= (len(string) - 1):
          if string[i].isdigit():
               digitCount = digitCount + 1
     
          i = i + 1

     return digitCount

##Take the string and return itself printed backwards
def reverseString(string):
     i = (len(string) -1)
     reversedString = ""
    
     while i >= 0:
          #Body
          reversedString = reversedString + string[i]
          
          #Update
          i = i - 1

     return reversedString
    
##Returns true if the string is a palindrome
def isPalindrome(word):
     
     reversedString = reverseString(word) #Call reverseString established above

     if word.upper() == reversedString.upper(): #Are they equivalent?
          return True
     else:
          return False
        
##Returns the middle character of an odd string, two middle characters if even
def middleChar(string):
     
     if len(string) < 1: #Proofing for a blank string input
          return ""
     
     if len(string) % 2 == 0:
          #Even
          character = string[(len(string) - 1) //2]
          character2 = string[((len(string) - 1) //2) + 1]
          return character + character2
     else:
          #Odd
          return string[(len(string) - 1) // 2]

##Repeats a phrase interspersed with a delimiter
def repeatPhrase(string, num, delim):
     i = 0
     finalString = ""
     
     while i < num:
          #Body
          finalString = finalString + string
          
          if i == (num - 1): #If we're on the last repetition, end the function early so an extra delim can't be added
               return finalString
          
          finalString = finalString + delim #Add the delim on if there are more repetitions to come
          
          #Update
          i = i + 1
          
     return finalString

##Checks against several parameters to determine if a given password is valid
def passwordCheck(password):
     i = 0
     digits = 0 #Amount of numbers in the password
     symbol = False #If there is a symbol used
     capital = False #If the user inputs a capital letter
     lowerCase = False #If the user inputs a lowerCase letter
     
     while i <= (len(password) - 1):
          #Body
          if password[i] in "!@#$%&*": #Check for symbols
               symbol = True
          if password[i].isupper():
               capital = True
          if password[i].islower():
               lowerCase = True          
          if password[i].isdigit():
               digits = digits + 1
          
          #Update
          i = i + 1
               
     print(digits)
     if digits >= 2 and symbol == True and capital == True and lowerCase == True and i >= 8: #Upper and lowercases, 2 digits, 8 or more total characters
          return True
     else:
          return False
     


     



        
        

        
