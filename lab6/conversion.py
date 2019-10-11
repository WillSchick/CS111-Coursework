#conversion
#Will Schick
#3/13/2018

print("--- "*6)

#Chart Setup
print("Celsius | Fahrenheit")
print("--------+-----------")

celsius = 0
while celsius < 100: 
    
    farenheight = (celsius * 1.8) + 32
    print("%8.0f|%10.0f" % (celsius,farenheight))
    
    #update
    celsius = celsius + 5
    