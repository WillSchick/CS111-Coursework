#William Schick
#3/3/2018
#This program will mimic the function of an ATM machine

#variables
balance = float(2000)

#logIn text
print("--- " * 5)
print("Welcome to the CS111 Bank")
print("Your current balance is $%.2f" % (balance))
print("Please choose either (D)eposit or (W)ithdrawal")
print()

#userInput
menuSelect = input(": ").upper()
print("--- " * 5)


#computation
if menuSelect == "D": #If the user selects deposit
    print("- Deposit Menu -")
    tempBalance = float(input("Enter deposit ammount: "))
    
    if tempBalance > 0:
        balance = (balance + tempBalance) #New balance is equal to the current balance modified by a deposit inputted by the user, so long as their input is > 0
    else:
        print("Error! Cannot deposit negative number!!")
    
elif menuSelect == "W": #If the user selects withdrawal
    print("- Withdrawal Menu -")
    tempBalance = float(input("Enter deposit ammount: "))
    
    if tempBalance > 0 and tempBalance <= balance:
        balance = (balance - tempBalance) #New balance is equal to the current balance modified by a withdrawal inputted by the user, os long as their input is > 0 and doesn't exceed current balance
    else:
        print("Error! Invalid choice!")
    
else: #If the use enters anything else, AKA an invalid input
    print("ERROR! Invalid choice!")
    

#Display current balance
if balance != 2000: #If the balance has been changed (aka no error)
    print("--- " * 5)
    print("Your current balance is $%.2f." % (balance))















