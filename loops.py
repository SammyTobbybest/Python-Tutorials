# print("1")
# print("2")
# print("3")
# print("4")
# print("5")
# print("6")
# print("7")
# print("8")
# print("9")
# print("10")

#For loops in python

# for num in range(0, 21):
#     print(num)


#While looops in python

# x = 0
# while x <= 10:
#     print(x)
#     x = x + 1





def addition(x, y):
    return x + y

def modulos(x, y):
    return x % y

def multiplication (x,y):
    return x * y

def subtraction ( x,y):
    return x - y

def division (x,y):
    return x/y


# ###################################

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter Second Number: "))

operator = input("Enter desired operator (+ - * / %): ")

if operator == "+":
    result = addition(num1, num2)

    print("The Sum is: ", result)

elif operator == "-":
    result = subtraction(num1,num2)

    print('The difference is: ', result)

elif operator == "/":
    result =  division (num1,num2)  

    print('The answer is:', result)

elif operator =="*":
    result = multiplication (num1,num2)
    print ("The answer is: ", result)

elif operator =="%":
    result = modulos(num1, num2)
    print ("The answer is: ", result)

else:
    print("error: nvalid operation")

