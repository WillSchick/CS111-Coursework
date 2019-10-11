#fileProcessing.py
#Will Schick
#4/18/2018
#
#Functions to process files.
#
#

##processStudents - example of reading from CSV, process student info and
## output to screen.
# parameter - The name, file must be csv
# return - none
def processStudents(studentFile):
    #open the file
    rFile = open(studentFile,"r")
    
    #Start reading
    line = rFile.readline()
    
    #loop through the entire file
    while line != "":
        # Process the line
        line = line.strip()     #Remove the white space
        data = line.split(",")  #Split on commas
        name = data[0]
        house = data[0]
        birthday = data[0]
        
        #output to console
        
        
        #update
        line = rFile.readline()
        
    rFile.close()










##fileTotalAverage - example of file reading and writing, calculated the
##total and the average of one file and output to another file.
# parameters - the name of the input, the name of the outputfile
# return - doesn't return as it simply writes to a file

def fileTotalAverage(inName, outName):
    # open the files
    readFile = open(inName, "r")
    writeFile = open(outName,"w")
    
    #init
    count = 0
    total = 0
    line = readFile.readline()
    
    # loop until the end of the file
    while line != "":
        # process the number and output to write file
        num = float(line)
        count = count + 1
        total = total + num
        
        #write the num to the output
        print(num)
        writeFile.write("%6.2f\n" % (num))
        
        #update
        line = readFile.readline()
    
    # calculate the average
    if count == 0:
        average = 0.0
    else:
        average = total / count
        
    # Finish the output
    writeFile.write("--------\n")
    writeFile.write("Total:   %6.2f\n" % (total))
    writeFile.write("Average: %6.2f\n" % (average))
    
    # Close the files
    readFile.close()
    writeFile.close()
    
        