#randomChar.py
#
# Will Schick
#
#2/22/2018
#
# This program randomly picks a character from the string and replicates it 25 times

#import ---
from random import *
from math import*

#User input and initialize prints ---
print( "--- " * 5)

word = input("Provide a word: ")
print("")
print("Original word: \"%s\"" % (word))
print("It is %d characters long!" % len(word))

print( "--- " * 5)

#The letter to be replicated ---
randCharacter = (randint(0,len(word)) - 1) #Takes a random int from 0, to the maximum length of the string,
letter = word[randCharacter] # This uses the random character from ^, and picks out the character that occurs in that spot in the string
print()
print(letter * 25)


