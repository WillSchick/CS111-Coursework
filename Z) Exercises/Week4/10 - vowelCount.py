#vowelCount
#Will Schick
#March 16, 2018


#Loop Init
string = input("Enter a string: ")
vowelCount = 0
while string != "":
    #Body
    
    #Innner loop init
    i = 0
    while i < len(string): #while string has letters
        #Body (count vowels inside the string)
        if string[i] in "AEIOUaeiou":
            vowelCount = vowelCount + 1
        #Innerloop update
        i = i+1
    
    
    #update
    string = input ("Enter another string: ")

print ("--- "*10)
print ("Total number of vowels!: ",vowelCount)