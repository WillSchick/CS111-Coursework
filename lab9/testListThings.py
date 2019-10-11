# testListThings.py
#
# Created by: R. Givens
# Modified by: Will Schick
#
# Tests the listThings module.
from listThings import *

def main():
    list1 = [10,17,5,-3,9,-27,5]
    list2 = [8, 12, -3, 5, -2]
    list3 = []
    
    #Test product
    print()
    print("Testing product")
    print("Want 3098250 2880 1\nHave", product(list1), product(list2), product(list3))
    print()
    
    #Test countOdds
    print()
    print("Testing countOdds")
    print(countOdds(list1))
    print(countOdds(list2))
    print(countOdds(list3))
    
    #Test squares
    print()
    print("Testing squares")
    print(squares(list1))
    print(squares(list2))
    print(squares(list3))
    
    #Test computeAltSum
    print()
    print("Testing computeAltSum")
    print(computeAltSum(list1))
    print(computeAltSum(list2))
    print(computeAltSum(list3))
    
    #Test replaceNegatives
    print()
    print("Testing replaceNegatives") 
    replaceNegatives(list1)
    replaceNegatives(list2)
    replaceNegatives(list3)
    print("Want [10, 17, 5, 0, 9, 0, 5] [8, 12, 0, 5, 0] []\nHave", (list1), (list2), (list3))
    print()         
    
    #Lists have been altered, so reassign
    list1 = [10,17,5,-3,9,-27,5]
    list2 = [8, 12, -3, 5, -2]
    list3 = []      
    
    #Test shiftRight
    print("Testing shiftRight")
    shiftRight(list1)
    print(list1)
    
    shiftRight(list2)
    print(list2)
    
    shiftRight(list3)
    print(list3)    
      

    
main()