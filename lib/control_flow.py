#!/usr/bin/env python3

# def admin_login(username, password):
#     if (username == "admin" or username == "ADMIN") and password == "12345":
#         return "Access Granted"
#     else:
#         return "Access Denied"
# username = input("Username : ")
# password = input("Password : ")
# result = admin_login(username, password)
# print(result)



# def hows_the_weather(temperature):
#     if (temperature < 40):
#         return "It's brisk out there!"
#     elif (temperature >= 40 and temperature <= 65):
#         return "It's a little chilly out there!"
#     elif (temperature > 85):
#         return "It's too dang hot out there!"
#     else:
#         return "It's perfect out there!"
    
# temperature = int(input("Temperature value: "))
# what_to_do = hows_the_weather(temperature)
# print(what_to_do)



# def fizzbuzz(num):
#     if (num % 3 == 0 and num % 5 == 0):
#         return "Fizz Buzz" 
#     elif (num % 3 == 0):
#         return "Fizz"
#     elif (num % 5 == 0):
#         return "Buzz"
#     else:
#         return num

# num = int(input("Enter a number : "))
# print(fizzbuzz(num))


def calculator(operation, num1, num2):
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num
    elif (operation == "*"):
        return num1 * num
    elif (operation == "/"):
        if num2 != 0:
            return num1 / num2
        else: 
            print ("Invalid operation")
            
    else:
        return None
    
operation = input("Enter an operation (+,-,*,/) : ")
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

result = calculator(operation, num1, num2)
print(result)        