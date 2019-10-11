# testGradeProcessing.py
#
# Created by: R. Givens
# Date: 4/24/2018
#
# Tests the file processing functions in gradeProcessing.pyt

from gradeProcessing import *

# uncomment test calls to test
def main():
    print()
    testGradeDistribution()
    testClassGrades()
    
    
def testGradeDistribution():
    print('***** Testing gradeDistribution("grades1.txt")')
    print("***** Grade distribution and histogram expected.\n")
    gradeDistribution("grades1.txt")
    print()
    
    print('***** Testing gradeDistribution("grades2.txt")')
    print("***** Grade distribution and histogram expected.\n")
    gradeDistribution("grades2.txt") 
    print()
    
    
def testClassGrades():
    print('***** Testing classGrades("class1.csv","class1-out.csv")')
    print("***** Check class1-out.csv for output!\n")
    classGrades("class1.csv","class1-out.csv")
    
    
    print('***** Testing classGrades("class2.csv","class1-out.csv")')
    print("***** Check class2-out.csv for output!\n")    
    classGrades("class2.csv","class2-out.csv")
    
    
main()
    

