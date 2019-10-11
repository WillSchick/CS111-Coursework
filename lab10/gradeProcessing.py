#gradeProcessing.py
#Will Schick
#4/24/2018


## opens and reads it, outputs a grade distribution and histogram (to the console)
# INPUT: Receives the name of the input file
# OUTPUT: Prints to console a histogram and distribution
def gradeDistribution(file):
    rFile = open(file,"r")
    
    #init
    i = 0 #init iteration (used for average at the end)
    gradeSum = [0, 0, 0, 0, 0] #A list containing number of letter grades [A, B, C, D, F]
    line = rFile.readline() #Read the first line
    
    #READING THE LINES ---------------------------------------------------------------------------
    while line != "": #Stop this loop when there are no more lines left to read    
        
        #Check each line against the grading code and add one to the corresponding letter grade
        if (float(line) >= 90):
            gradeSum[0] = gradeSum[0] + 1
        elif (float(line) >= 80):
            gradeSum[1] = gradeSum[1] + 1
        elif (float(line) >= 70):
            gradeSum[2] = gradeSum[2] + 1
        elif (float(line) >= 60):
            gradeSum[3] = gradeSum[3] + 1
        else:
            gradeSum[4] = gradeSum[4] + 1
        
        #update
        i = i + 1 #Increase iteration (used for average at the end)
        line = rFile.readline() #Advance to the next line
    
    #Grade distribution
    #Use the i from before to get the average of each grade
    print("Grade Distribution:")
    print("A: %5.2f" % ((gradeSum[0] / i)*100) + "%")
    print("B: %5.2f" % ((gradeSum[1] / i)*100) + "%")
    print("C: %5.2f" % ((gradeSum[2] / i)*100) + "%")
    print("D: %5.2f" % ((gradeSum[3] / i)*100) + "%")
    print("F: %5.2f" % ((gradeSum[4] / i)*100) + "%")
    print()
    
    #Grade Histogram
    #Replicate an asterisk for every percentage point
    print("Grade Histogram:")
    print("A:", "*" * (100 * gradeSum[0] // i))
    print("B:", "*" * (100 * gradeSum[1] // i))
    print("C:", "*" * (100 * gradeSum[2] // i))
    print("D:", "*" * (100 * gradeSum[3] // i))
    print("F:", "*" * (100 * gradeSum[4] // i))
    
    
    #Epilogue
    rFile.close()
    return






##CLASS GRADES ---------------------------------------------------------------
def classGrades(inFile,outFile):
    rFile = open(inFile,"r")
    wFile = open(outFile,"w")
    
    #init
    line = rFile.readline() #Read the first line
    
    while line != "":
        line.strip()
        data = line.split(",") #Create a list deliminated by ","
        
        name = data[0]
        
        #Init average calculation
        gradeSum = 0
        for i in range(1,len(data)): #Loops through the line (After the name!).
            gradeSum = gradeSum + float(data[i]) #Add all of the grades together
            average = gradeSum / i #Divide the grade total by the amount of grades, achieving average
        
        #Grade calculation
        if (average >= 90): #if the kid has an A
            grade = "A" #Assign their grade score to A
        elif (average >= 80): #repeat for all the other grades
            grade = "B"
        elif (average >= 70): 
            grade = "C"
        elif (average >= 60): 
            grade = "D"
        else:
            grade = "F"
        
        #WRITE TO THE OUTPUT FILE
        wFile.write(name +  "," + str(average) + "," + grade) #For instance: "Sally, 99.2, A" 
        wFile.write("\n")
        
        #Update
        line = rFile.readline() #Move on to the next line and repeat until no more lines
        
         
    
    #Epilogue
    rFile.close()
    wFile.close()
    return

    