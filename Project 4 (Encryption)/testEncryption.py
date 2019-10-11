# testEncryption.py
# Created by: R. Givens
# Description: Tests all the functions in fileEncryption.py.  
# Requires no user input.

from encryption import *

def main():
    # comment out until you are ready to test
    #testEncryptChar()
    #testDecryptChar()
    #testEncryptDigit()
    #testDecryptDigit()
    #testConvertString()
    testConvertFile()
    return
    
    

def testEncryptChar():
    print("*******************************")
    print("***** Testing encryptChar *****")
    print("*******************************")
    print()    
    
    n1 = 3
    n2 = 11
    
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("Orig.", "Expec.", "n = 3", "Orig.", "Expec.", "n = 11"))
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("-"*6, "-"*6, "-"*6, "-"*6, "-"*6, "-"*6))   
    
    expected1 = "defghijklmnopqrstuvwxyzabc" 
    expected2 = "LMNOPQRSTUVWXYZABCDEFGHIJK"
    
    for i in range(26):
        # use constant LETTERS from fileEncryption
        lett1 = LETTERS[i]
        lett2 = LETTERS[i].upper()
        exp1 = expected1[i]
        exp2 = expected2[i]
        encr1 = encryptChar(lett1, n1)
        encr2 = encryptChar(lett2, n2)
        print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" %  (lett1, exp1, encr1, lett2, exp2, encr2))
        
    print()
        
    
def testDecryptChar():
    print("*******************************")
    print("***** Testing decryptChar *****")
    print("*******************************")
    print()      
    
    n1 = 3
    n2 = 11
    
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("Orig.", "Expec.", "n = 3", "Orig.", "Expec.", "n = 11"))
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("-"*6, "-"*6, "-"*6, "-"*6, "-"*6, "-"*6))   
    
    encr1 = "defghijklmnopqrstuvwxyzabc" 
    encr2 = "LMNOPQRSTUVWXYZABCDEFGHIJK"
    
    for i in range(26):
        # use constant LETTERS from fileEncryption
        lett1 = encr1[i]
        lett2 = encr2[i]
        exp1 = LETTERS[i]
        exp2 = LETTERS[i].upper()
        decr1 = decryptChar(lett1, n1)
        decr2 = decryptChar(lett2, n2)
        print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" %  (lett1, exp1, decr1, lett2, exp2, decr2))
        
    print()

def testEncryptDigit():
    print("********************************")
    print("***** Testing encryptDigit *****")
    print("********************************")
    print()    
    
    n1 = 7
    n2 = 4
       
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("Orig.", "Expec.", "n = 7", "Orig.", "Expec.", "n = 4"))
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("-"*6, "-"*6, "-"*6, "-"*6, "-"*6, "-"*6))   
    
    expected1 = [7,8,9,0,1,2,3,4,5,6]  
    expected2 = [4,5,6,7,8,9,0,1,2,3]
    
    for i in range(10):
        dig1 = i
        dig2 = i
        exp1 = expected1[i]
        exp2 = expected2[i]
        encr1 = encryptDigit(dig1, n1)
        encr2 = encryptDigit(dig2, n2)
        print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" %  (dig1, exp1, encr1, dig2, exp2, encr2))
        
    print()

def testDecryptDigit():
    print("********************************")
    print("***** Testing decryptDigit *****")
    print("********************************")
    print()    
    
    n1 = 7
    n2 = 4
       
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("Orig.", "Expec.", "n = 7", "Orig.", "Expec.", "n = 4"))
    print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" % ("-"*6, "-"*6, "-"*6, "-"*6, "-"*6, "-"*6))   
    
    encr1 = [7,8,9,0,1,2,3,4,5,6]  
    encr2 = [4,5,6,7,8,9,0,1,2,3]
    
    for i in range(10):
        dig1 = encr1[i]
        dig2 = encr2[i]
        exp1 = i
        exp2 = i
        decr1 = decryptDigit(dig1, n1)
        decr2 = decryptDigit(dig2, n2)
        print("%-6s  %-6s  %-6s | %-6s  %-6s  %-6s" %  (dig1, exp1, decr1, dig2, exp2, decr2))
        
    print()

def testConvertString():
    print("*********************************")
    print("***** Testing convertString *****")
    print("*********************************")
    print()
    n = 17
    
    print("n = 17\n")

    strings = ["Hello World!", "82 elephants.", "HEFFELUMPS and WOOZLES", "3 Bippity-Boppity-Boos"]
    expected = ["Yvccf Nficu!", "59 vcvgyrekj.", "YVWWVCLDGJ reu NFFQCVJ", "0 Szggzkp-Sfggzkp-Sffj"]
    
    print("***** Encrypting *****")
    for i in range(len(strings)):
        string = strings[i]
        want = expected[i]
        result = convertString(string, n, True)
        print("Original: ", string)
        print("Expected: ", want)
        print("Actual:   ", result)
        print()
    
    print("***** Decrypting *****")
    for i in range(len(strings)):
        string = expected[i]
        want = strings[i]
        result = convertString(string, n, False)
        print("Original: ", string)
        print("Expected: ", want)
        print("Actual:   ", result)
        print()    
    
    

def testConvertFile():
    print("*********************************")
    print("***** Testing convertString *****")
    print("*********************************")
    print()
    
    n = 8
    
    print("n = 8\n")
    
    convertFile("tisket.txt", "encrypted.txt", n, True)
    convertFile("encrypted.txt", "decrypted.txt", n, False)
    
    print("tisket.txt and decrypted.txt should contain the same text")
    print()
    print("encrypted.txt should contain:\n")
    print("I-bqasmb I-biasmb,")
    print("I jzwev ivl gmttwe jiasmb.")
    print("Q amvl i tmbbmz bw ug uwuug")
    print("Wv bpm eig Q lzwxxml qb.")
    print("Q lzwxxml qb!")
    print("Q lzwxxml qb!")
    print("Gma wv bpm eig Q lzwxxml qb!")
    print("I tqbbtm oqztqm xqksml qb cx,")
    print("Ivl xcb qb qv pmz xwksmb.")  

main()
    
    