# dog = "hungry"
# if dog == "hungry":
#     owner = "feed the dog"
# elif dog == "thirsty":
#     owner = "refill the water bowl"
# elif dog == "playful":
#     owner = "play with the dog"
# else:
#     owner = "dog is boring"
# print(owner)


dog = input("what is the dog's condition? : ")
dict_map = {
    "hungry": "feed the dog",
    "thirsty": "refill the water bottle",
    "playful": "play with the dog",
}
owner = dict_map.get(dog, "dog is boring") #.get method lets us set a default value
print(owner)


# age = int(input('enter age:'))
# if age < 2:
#     is_baby = "baby"
# else:
#     is_baby = "not baby"
# print("The person is:",is_baby)

# def divide (num1, num2):
#     try:
#         quotient = num1//num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot contain 0")
#     except TypeError:
#         print("Error: input must be int or str")
#     finally:
#         print("Isn't division fun?")
# divide(5,4)
