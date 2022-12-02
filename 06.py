# if [0]:
#     print("This is true.")  # works, because list has an object.

# if 0:
#     print("This is true")  # Doesn't work, because 0 is false.

# if ["Ali"]:
#     print("This is true")  #It works, list has an integer object.


# grocery_store = ["meat", "onion", "bread"]
# if "meat" and "bread" and "lettuce" or "onion" in grocery_store:
#     print("Bon appetit")


# empty_seat = 54
# if empty_seat > 0:
#     print ("oldukca yerimiz mevcut")

# x = 6
# y = 9

# print('is x equal to y?				:', x == y)
# print('is x not equal to y?			:', x != y)
# print('is x less than y?				:', x < y)
# print('is x greater than y?			:', x > y)
# print('is x less than or equal to y?		:', x <= y)
# print('is x greater than or equal to y?		:', x >= y)

# first_set = set("TWELVE PLUS ONE")
# second_set = set("ELEVEN PLUS TWO")
# if first_set == second_set:
#     print ("We are the same!")

# number = 5
# if number <= 3:
#     print("Number is smaller than or equal to 3")
# else:
#     print("Number is bigger than 3")

# number = 49
# if number >= 72:
#     print(f"{number} is bigger than or equal to 72")
# else:
#     print(f"{number} is smaller than 72")


# number = int(input("Bir sayı giriniz: "))
# if number %2 == 0:
#     print(f"{number} bir çift sayıdır.")
# else:
#     print(f"{number} bir tek sayıdır.")

# number = float(input("Enter a positive or negative number: "))

# if number < 0:
#     print(f"{number} is a negative number.")
# elif number == 0:
#     print(f"{number} is neither positive nor negative")
# else:
#      print(f"{number} is a positive number.")


# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter another number: "))

# if number1 > number2:
#     print (f"{number1} is greater than {number2}")
# else:
#     print(f"{number1} is smaller than {number2}")


# audience = "baby"
# if audience == "kid":
#     print("Free to go to cinema.")
# elif audience == "teen":
#     print("discounted price")
# elif audience == "adult":
#     print("Normal price")
# else:
#     print("No such audience")


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 > num2 and num3:
#     print (f"{num1} is the greatest number.")
# elif num2 > num3 and num1:
#     print(f"{num2} is the greatest number.")
# else:
#     print(f"{num3} is the greatest number.")


# num1 = int(input("Enter the first number: "))

# if num1 > 0:
#     print (f"{num1} is a positive number")
# elif num1 < 0:
#     print(f"{num1} is a negative number.")
# else:
#     print(f"{num1} is zero.")


# audience_group = "kid", "teen", "adult"
# audience = "old"
# if audience in audience_group:
#     if audience == "kid":
#         print("It is free to go to the cinema.")
#     elif audience == "teen":
#         print("Discounted price")
#     else:  # audience == adult
#         print("Normal price")
# else:
#     print("There is no such a group.")
