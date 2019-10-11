from temp import Temperature

def main():
    temp1 = Temperature()
    
    #Test Getters
    print("Testing getCelsius() and getFahrenheit().")
    print("Celsius temperuture should be 0.00  and is %.2f" % temp1.getCelsius())
    print("Fahren. temperature should be 32.00 and is %.2f" % temp1.getFahrenheit())
    print()
    
    #Test setCelsius, needs getCelsius and getFahrenheit to test
    print("Testing setCelsius.")
    temp1.setCelsius(15.2)
    print("Celsius temperuture should be 15.20 and is %.2f" % temp1.getCelsius())
    print("Fahren. temperature should be 59.36 and is %.2f" % temp1.getFahrenheit())
    print()
    
    #Test setFahrenheit, needs getCelsius and getFahrenheit to test
    print("Testing setFahrenheit.")
    temp1.setFahrenheit(92.5)
    print("Celsius temperuture should be 33.61 and is %.2f" % temp1.getCelsius())
    print("Fahren. temperature should be 92.50 and is %.2f" % temp1.getFahrenheit())
    print()
    
    #Test string representation, needs setCelsius and setFahrenheit to test
    print("Testing string representation.")
    temp2 = Temperature()
    print("Should be  0.00 C and is %7s" % temp2)
    temp2.setCelsius(16.73456)
    print("Should be 16.73 C and is %7s" % temp2)
    temp2.setFahrenheit(71.45)
    print("Should be 21.92 C and is %7s" % temp2)
    
    
    
    
    
    
main()
    