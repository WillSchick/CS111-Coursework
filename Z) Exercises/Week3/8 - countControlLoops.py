#countControlLoops.py
#Will Schick
#3/12/2018

#Initialization
count = 1
final = int(input("Enter your final value: "))
theSum = 0

#Condition
while count <= final:
    #body
    theSum = theSum + count
    
    #update
    count = count + 1
    
#print the final sum
print("Sum from",1,"to",final,"is",theSum)