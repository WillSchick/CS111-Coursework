# testStringThings.py
#
# Created by: R. Givens
# Modified by:
#
# Tests the stringThings module.
from stringThings import *


#test stringThings
def main():
    print()
    
    #test countDigits()
    print("***** Testing countDigits *****")
    print('countDigits("a1b2c3d4e5f6g7h8i9j0") should return 10  actually returns %2d' % (countDigits("a1b2c3d4e5f6g7h8i9j0")))
    print('countDigits("The year 1984")        should return  4  actually returns %2d' % (countDigits("The year 1984")))
    print('countDigits("Elephants.")           should return  0  actually returns %2d' % (countDigits("Elephants.")))
    print()    
    
    #test reverseString()
    print("***** Testing reverseString *****")
    print('reverseString("racecar")  should return "racecar"  actually returns "%s"' % str(reverseString("racecar")))
    print('reverseString("elephant") should return "tnahpele" actually returns "%s"' % str(reverseString("elephant")))
    print('reverseString("")         should return ""         actually returns "%s"' % str(reverseString("")))
    print()     
    
    #test isPalindrome()
    print("***** Testing isPalindrome *****")
    print('isPalindrome("racecar")  should return True  actually returns %s' % str(isPalindrome("racecar")))
    print('isPalindrome("elephant") should return False actually returns %s' % str(isPalindrome("elephant")))
    print('isPalindrome("")         should return True  actually returns %s' % str(isPalindrome("")))
    print()     
       
    #test middleChar()
    print("***** Testing Middle *****")
    print('middleChar("stupefy")    should return "p"  actually returns "%s"' % middleChar("stupefy"))
    print('middleChar("levicorpus") should return "co" actually returns "%s"' % middleChar("levicorpus")) 
    print('middleChar("")           should return ""   actually returns "%s"' % middleChar("")) 
    print()
    
    #test repeatPhrase()
    print("***** Testing Repeat *****")
    print('repeatPhrase("pew",3,"-")    should return "pew-pew-pew" actually returns "%s"' % repeatPhrase("pew",3,"-"))
    print('repeatPhrase("yay",1,"!!!!") should return "yay"         actually returns "%s"' % repeatPhrase("yay",1,"!!!!"))
    print('repeatPhrase("hey",-1," ")   should return ""            actually returns "%s"' % repeatPhrase("hey",-1," ") )
    print() 
    
    #test passwordCheck()
    print("***** Testing passwordCheck *****")
    print('passwordCheck("aB#12")        should return False actually returns %s' % str(passwordCheck("aB#12")))
    print('passwordCheck("abcDEF123**")  should return True  actually returns %s' % str(passwordCheck("abcDEF123**")))
    print('passwordCheck("ABCDEF123!!")  should return False actually returns %s' % str(passwordCheck("ABCDEF123!!")))
    print('passwordCheck("abcdef123$$")  should return False actually returns %s' % str(passwordCheck("abcdef123$$")))
    print('passwordCheck("abcdefGHI@@")  should return False actually returns %s' % str(passwordCheck("abcdefGHI@@")))
    print('passwordCheck("abcDEF12345")  should return False actually returns %s' % str(passwordCheck("abcDEF12345")))
    print()     
    
    
  
    

    
    
    
    
    
    
#call main
main()