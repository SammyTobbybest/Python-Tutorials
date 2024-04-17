# num1 = int(input("Enter num1: "))
# num2= int(input("Enter num2: "))

# print("Num1 is ", num1, "and Num2 is: ", num2)
# print("Num1 is %d and Num2 is %d", num1, num2)


# def SayHello(username):
#     print("Hello ", username)


# #Main code
# user_name = input("Enter your name: ")

# SayHello(user_name)


# def addition(x, y):
#     return x + y

# def modulos(x, y):
#     return x % y

# def multiplication (x,y):
#     return x * y

# def subtraction ( x,y):
#     return x - y

# def division (x,y):
#     return x/y




# ###################################

# num1 = int(input("Enter first Number: "))
# num2 = int(input("Enter Second Number: "))

# operator = input("Enter desired operator (+ - * / %): ")

# if operator == "+":
#     result = addition(num1, num2)

#     print("The Sum is: ", result)

# elif operator == "-":
#     result = subtraction(num1,num2)

#     print('The difference is: ', result)

# elif operator == "/":
#     result =  division (num1,num2)  

#     print('The answer is:', result)

# elif operator =="*":
#     result = multiplication (num1,num2)
#     print ("The answer is: ", result)

# elif operator =="%":
#     result = modulos(num1, num2)
#     print ("The answer is: ", result)

# else:
#     print("error: nvalid operation")



# def AreaRec(length, width):
#     answer = length * width
#     return answer





###############
def Areatrgl (base,height):
    answer = (1/2 * base ) * height
    return answer



base = int(input("enter base of triangle"))
height = int(input("enter height of triangle"))

area = Areatrgl(base, height)


print("The Area is: ", area)
