def addition():
    print("********* Addition Operation Selected **********")
    print('')
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 + num2
    print("The Sum of ", num1, " and ", num2, " is", result)

def subtraction():
    print("********* Subtraction Operation Selected **********")
    print('')
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 - num2
    print("The difference of ", num1, " and ", num2, " is", result)

def multiplication():
    print("********* Multiplication Operation Selected **********")
    print('')
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 * num2
    print("The product of ", num1, " and ", num2, " is", result)

def division():
    print("********* Division Operation Selected **********")
    print('')
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    #Using while loop to check if num2 is = 0
    while num2 == 0:
        print("Error: You cannot divide by 0. Enter another number")
        print('')
        num2 = int(input("Enter the Number again: "))
        


    result = num1 / num2
    print("The division of ", num1, " and ", num2, " is", result)

def modulo():
    print("********* Modulo Operation Selected **********")
    print('')
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 % num2
    print("The Modulo of ", num1, " and ", num2, " is", result)

def OptionChecker(option):
    if option == "1":
        addition()
    elif option == "2":
        subtraction()
    elif option == "3":
        multiplication()
    elif option == "4":
        division()
    elif option == "5":
        modulo()
    elif option == "6":
        print("Program Exiting .......")
    else:
        print("Error: Invalid Option Entered")



print('')
print('')
print("************** Welcome to The Best Calculator Program ****************")
print('')
print("Menu --- Select one of the options below to perform an operation")
print('')
print('')

print("1- Addition(+)")
print("2- Subtraction(-)")
print("3- Multiplication(*)")
print("4- Division(/)")
print("5- Modulo(%)")
print("6- Exit")

print('')
option = input("Enter Option: ")

OptionChecker(option)

print('')
choice = input("Do you want to continue (Y/N)")

while choice == "Y":
    print('')
    print("Menu --- Select one of the options below to perform an operation")
    print('')
    print('')

    print("1- Addition(+)")
    print("2- Subtraction(-)")
    print("3- Multiplication(*)")
    print("4- Division(/)")
    print("5- Modulo(%)")
    print("6- Exit")

    print('')
    option = input("Enter Option: ")

    OptionChecker(option)

    print('')
    choice = input("Do you want to continue (Y/N)")
    











