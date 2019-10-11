#ListAlgorithms.py
#Will Schick
#4/1/6/2018

##getGreaterTahn - example of building up a new list (based on matches),
## create a new list containing all the numbers greater than a limit
def getGreaterThan(values,limit):
    #setup
    i = 0
    newList = []
    
    while i < len(values):
        
        if values[i] > limit:
            newList.append(values[i])
        
        #Update
        i = i + 1    

    return newList

##countGreaterThan - example of counting matches, count numbers greater than
## A limit
#Parameters- Receive a list of values, and a limit
#Return - The count
def countGreaterThan(values,limit):
    #Setup
    i = 0
    count = 0
    
    #loop through the indicies
    while i < len(values):
        #item equivalent to the values at the index
        item = values[i]
        
        # test
        if item > limit:
            count = count + 1
        
        #Update
        i = i + 1
        
    return count
        
        
def main():
    
    listy = [0, -2, 12, 7 , -5, 8, 15, 27, 102, 1]
    
    print(countGreaterThan(listy, 10))
    print(getGreaterThan(listy,10))
    
main()