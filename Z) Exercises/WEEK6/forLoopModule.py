

def countByFives(target):
    for i in range(5,target + 1,5):
        print(i)
    return
        
        
def sumFrom(target):
    sum = 0 
    for i in range(target + 1):
        sum = sum + i
        
    return sum


def countVowels(string):
    vowelSum = 0
    for i in range(len(string)):
        if string[i] in "AEIOUaeiou":
            vowelSum = vowelSum + 1
    return vowelSum


def countDigits(string):
    digitSum = 0
    for char in string:
        if char.isdigit():
            digitSum = digitSum + 1
    return digitSum

print(countDigits("Wow101Wow"))

