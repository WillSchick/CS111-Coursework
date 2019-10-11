#factorial
#Will Schick
#3/13/2018
#This program will ask the user for a positive input from the user and calculate the factorial of that number using a loop
print ("--- " * 6)

#input
countTo = int(input("Input a number: "))

if countTo < 0:
    print("No negative numbers please!")
else:
    

    #Loop set up
    count = 1
    factorial = 1

    #Loop
    while count <= countTo:
    
        #Do stuff
        factorial = factorial * count #Multiply the current sum by the next number in the cycle
    
        #update
        count = count + 1
    
    
    #Print results
    print ("Factorial of", str(countTo) + ": ", factorial)