#Count Vowel Functions
#Will Schick
#3/26/2018
print()

def main():
    getStrings()
    

def outputCount(count):
    print("There are", count, "vowels.")
    return

##countVowels: count the vowels in a string
# Param: a string
# return: count
def countVowels(string):
    i = 0
    count = 0
    
    while i < len(string):
        char = string[i]
        if char.lower() in "aeiou":
            count = count + 1
        i = i + 1
    
    return count

## Get strings from user------------------------------------------------------------
def getStrings():
    print("Enter nothing to stop.")
    total = 0
    string = input("Enter a string: ")
    while string != "": #When the user inputs nothing- cancel the loop
        string = input("Enter another string: ")
        total = total + countVowels(string)
    
    print(outputCount(total))


#MAIN MAIN MAIN GUCCI GUCCI GUCCI GUCCI MAIN MAIN MAIN MAIN-----------------------------
main()
        