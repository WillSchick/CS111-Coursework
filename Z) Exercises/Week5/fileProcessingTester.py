#fileProcessingTester.py
#Will Schick
#4/18/2018
#
# Tester for our file processing functions.

from fileProcessing import *

def main():
    print("Testing the function fileTotalAverage")
    fileTotalAverage("numbers.txt","out-numbers.txt")
    print("fileTotalAverage is done.")
    

main()
    