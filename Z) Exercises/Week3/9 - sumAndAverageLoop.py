#sumAndAverageLoop
#Will Schick
#March 13, 2018

#Sum and average user data


#Init
sumTotal = 0
count = 0
userInput = input("Enter a value: ")

#Stop when user enters an empty string
while userInput != "":
    #body
    value = float(userInput)
    sumTotal = sumTotal + value
    
    if count == 0:
        minimum = userInput
        maximum = userInput
    else:
        if minimum > userInput:
            minimum = userInput
        if maximum < userInput:
            maximum = userInput        
    
    # update
    userInput = input("Enter another value: ")
    count = count + 1
    
print()
print("---Results---")
print("The sum is:", sumTotal)
print("The minimum is:", minimum)
print("The maximum is:", maximum)

if count == 0:
    average = 0.0
else:
    average = sumTotal / count

print("The average is:", average)