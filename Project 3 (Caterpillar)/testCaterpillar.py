from caterpillar import *


def main():
    #testDrawCaterpillar()
    #testRollDie()
    #testIsCompleteCaterpillar()
    #testUseAntenna()
    #testUseHead()
    #testUseBody()
    #testUseLeg()
    #testPlayGame()

def testDrawCaterpillar():
    name = "Testing drawCaterpillar()"
    print()
    print("*"*(len(name)+10))
    print("****", name, "****")
    print("*"*(len(name)+10))
    print()
    
    
    #No parts
    print("-"*15)
    print("Expected: ")
    print("\n")
    print("Actual:  ")
    drawCaterpillar(0,0,0,0)
    
    #One body
    print("-"*15)
    print("Expected: ")
    print("\n      * * *\n")
    print("Actual:  ")
    drawCaterpillar(0,0,1,0)
    
    #One body, one head, 2 legs
    print("-"*15)
    print("Expected: ")
    print("\n          O\n      * * *\n        | |\n")
    print("Actual:  ")
    drawCaterpillar(0,1,1,2)    
    
    #two bodies, one head, 4 legs, one antenna
    print("-"*15)
    print("Expected: ")
    print("\n         \\\n          O\n* * *-* * *\n    | | | |\n")
    print("Actual:  ")
    drawCaterpillar(1,1,2,4)   
    
    #complete
    print("-"*15)
    print("Expected: ")
    print("\n         \\ /\n          O\n* * *-* * *\n| | | | | |\n")
    print("Actual:  ")
    drawCaterpillar(2,1,2,6)   
    
    print("-"*15)
    
    
def testRollDie():
    name = "Testing rollDie()"
    print()
    print("*"*(len(name)+10))
    print("****", name, "****")
    print("*"*(len(name)+10))
    print()
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    
    loopCount = 0
    while(loopCount < 600):
        roll = rollDie()
        if roll == 1:
            count1 = count1 + 1
        elif roll == 2:
            count2 = count2 + 1
        elif roll == 3:
            count3 = count3 + 1
        elif roll == 4:
            count4 = count4 + 1
        elif roll == 5:
            count5 = count5 + 1
        elif roll == 6:
            count6 = count6 + 1
        loopCount = loopCount + 1
    
    print()        
    print("Out of 600 rolls", count1 + count2 + count3 + count4 + count5 + count6, "were between 1 and 6.")
    print("\nExpect about 100 rolls each. (85-115)")
    print("Roll of 1: %3d"% count1)
    print("Roll of 2: %3d"% count2)
    print("Roll of 3: %3d"% count3)
    print("Roll of 4: %3d"% count4)
    print("Roll of 5: %3d"% count5)
    print("Roll of 6: %3d"% count6)
    print()
    

def testIsCompleteCaterpillar():    
    name = "Testing isCompleteCaterpillar()"
    print()
    print("*"*(len(name)+10))
    print("****", name, "****")
    print("*"*(len(name)+10))
    print()
    
    
    #No parts
    print("-"*15)
    drawCaterpillar(0,0,0,0)
    print("Expected: False")
    print("Actual:  ", isCompleteCaterpillar(0,0,0,0))
    print()
    
    #One body
    print("-"*15)
    drawCaterpillar(0,0,1,0)
    print("Expected: False")
    print("Actual:  ", isCompleteCaterpillar(0,0,1,0))
    print()
    
    #One body, one head, 2 legs
    print("-"*15)
    drawCaterpillar(0,1,1,2)
    print("Expected: False")
    print("Actual:  ", isCompleteCaterpillar(0,1,1,2))
    print()  
    
    #two bodies, one head, 4 legs, one antenna
    print("-"*15)
    drawCaterpillar(1,1,2,4)
    print("Expected: False")
    print("Actual:  ", isCompleteCaterpillar(1,1,2,4))
    print()
    
    #complete
    print("-"*15)
    drawCaterpillar(2,1,2,6)
    print("Expected: True")
    print("Actual:  ", isCompleteCaterpillar(2,1,2,6))
    print()
    
    print("-"*15)

def testUseAntenna():
    name = "Testing useAntenna()"
    print()
    print("*"*(len(name)+10))
    print("****", name, "****")
    print("*"*(len(name)+10))
    print()
    
    # no head
    print("-"*45)
    drawCaterpillar(0,0,2,6)
    print("Expected:")
    print("You can't have an antenna without a head!")
    print("Actual:")
    result = useAntenna(0,0,2,6)
    print("Expected: False")
    print("Actual:  ", result)
    print()
    
    
    # 1 head
    print("-"*45)
    drawCaterpillar(0,1,2,6)
    print("Expected:")
    print("You got an antenna!")
    print("Actual:")
    result = useAntenna(0,1,2,6)
    print("Expected: True")
    print("Actual:  ", result)
    print()
    
    # 1 head, 1 antenna
    print("-"*45)
    drawCaterpillar(1,1,2,6)
    print("Expected:")
    print("You got an antenna!")
    print("Actual:")
    result = useAntenna(1,1,2,6)
    print("Expected: True")
    print("Actual:  ", result)
    print()
    
    # 1 head, 2 antenna
    print("-"*45)
    drawCaterpillar(2,1,2,6)
    print("Expected:")
    print("You've already got antenna.")
    print("Actual:")
    result = useAntenna(2,1,2,6)
    print("Expected: False")
    print("Actual:  ", result)
    print()
    
    print("-"*45)

def testUseHead():
    name = "Testing useHead()"
    print()
    print("*"*(len(name)+10))
    print("****", name, "****")
    print("*"*(len(name)+10))
    print()
    
    # no body
    print("-"*45)
    drawCaterpillar(0,0,0,0)
    print("Expected:")
    print("You can't have a head without a body.")
    print("Actual:")
    result = useHead(0,0,0,0)
    print("Expected: False")
    print("Actual:  ", result)
    print()
    
    # one body
    print("-"*45)
    drawCaterpillar(0,0,1,3)
    print("Expected:")
    print("You got a head!")
    print("Actual:")
    result = useHead(0,0,1,3)
    print("Expected: True")
    print("Actual:  ", result)
    print()    
    
    # two bodies
    print("-"*45)
    drawCaterpillar(0,0,2,6)
    print("Expected:")
    print("You got a head!")
    print("Actual:")
    result = useHead(0,0,2,6)
    print("Expected: True")
    print("Actual:  ", result)
    print() 
    
    # 1 head
    print("-"*45)
    drawCaterpillar(0,1,2,6)
    print("Expected:")
    print("You've already got a head.")
    print("Actual:")
    result = useHead(0,1,2,6)
    print("Expected: False")
    print("Actual:  ", result)
    print() 
    
    print("-"*45)

def testUseBody():
    name = "Testing useBody()"
    print()
    print("*"*(len(name)+10))
    print("****", name, "****")
    print("*"*(len(name)+10))
    print()
    
    # no body
    print("-"*45)
    drawCaterpillar(0,0,0,0)
    print("Expected:")
    print("You got a body!")
    print("Actual:")
    result = useBody(0,0,0,0)
    print("Expected: True")
    print("Actual:  ", result)
    print()
    
    # one body
    print("-"*45)
    drawCaterpillar(0,0,1,3)
    print("Expected:")
    print("You got a body!")
    print("Actual:")
    result = useBody(0,0,1,3)
    print("Expected: True")
    print("Actual:  ", result)
    print()    
    
    # two bodies
    print("-"*45)
    drawCaterpillar(0,0,2,6)
    print("Expected:")
    print("You've already got your body segments.")
    print("Actual:")
    result = useBody(0,0,2,6)
    print("Expected: False")
    print("Actual:  ", result)
    print() 
    
    print("-"*45)

def testUseLeg():
    name = "Testing useLeg()"
    print()
    print("*"*(len(name)+10))
    print("****", name, "****")
    print("*"*(len(name)+10))
    print()
    
    # no body
    print("-"*45)
    drawCaterpillar(0,0,0,0)
    print("Expected:")
    print("You need another body segment for this leg.")
    print("Actual:")
    result = useLeg(0,0,0,0)
    print("Expected: False")
    print("Actual:  ", result)
    print()
    
    # one body
    count = 0 
    while count < 3:
        print("-"*45)
        drawCaterpillar(0,0,1,count)
        print("Expected:")
        print("You got a leg!")
        print("Actual:")
        result = useLeg(0,0,1,count)
        print("Expected: True")
        print("Actual:  ", result)
        print()    
        count = count + 1
        
    print("-"*45)
    drawCaterpillar(0,0,1,3)
    print("Expected:")
    print("You need another body segment for this leg.")
    print("Actual:")
    result = useLeg(0,0,1,3)
    print("Expected: False")
    print("Actual:  ", result)
    print()   
    
    # two body
    count = 0 
    while count < 6:
        print("-"*45)
        drawCaterpillar(0,0,2,count)
        print("Expected:")
        print("You got a leg!")
        print("Actual:")
        result = useLeg(0,0,2,count)
        print("Expected: True")
        print("Actual:  ", result)
        print()    
        count = count + 1
        
    print("-"*45)
    drawCaterpillar(0,0,2,6)
    print("Expected:")
    print("You've already got all your legs.")
    print("Actual:")
    result = useLeg(0,0,2,6)
    print("Expected: False")
    print("Actual:  ", result)
    print()    
    
    print("-"*45)

def testPlayGame():
    playGame()
    
main()