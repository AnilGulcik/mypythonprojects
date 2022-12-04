# number = 0
# while number < 6:
#     print(number)
#     number += 1

# print ("Now, number is bigger or equal to 6")


# my_list = ["a", "b", "c", "d", "e"]
# a = 0

# while a < len(my_list):
#     print(f"square of {a} is : {a ** 2}")
#     a += 1

# age = input("Enter your age please : ")
# while not age.isdigit():
#     print("You entered incorrectly!")
#     age = input ("Please enter your age again: ")
# print(f"Well done! Your age is {age}")

# answer = 57

# question = "Which number am I thinking of? "
# print("Lets play the guessing game!")

# while True:
#     guess = int(input(question))
    
#     if guess < answer:
#         print("Little higher")
#     elif guess > answer:
#         print("little lower")
#     else:
#         print("Are you a mindreader?!!")
#         break


# import random
# coin = ("yazi", "tura")
# yazi, tura = 0, 0
# games = 0
# print("Cikmak icin x e basiniz")

# while True:
#     flip = random.choice(coin)
#     your_choice = input("Yazi mi Tura mi?").lower()
#     if your_choice == "x":
#         print("GAME OVER")
#         print("Oyun istatistikleri: ")
#         print(f"Kac kere oynadiniz: {games}")
#         print(f"Kac kere yazi geldi: {yazi}")
#         print(f"Kac kere tura geldi: {tura}")
#         break
#     if your_choice == flip:
#         print(f"Para {flip} geldi. Bravo!")
#         games += 1
#     else:
#         print(f"Para {flip} geldi. Tekrar deneyiniz.")
#         games += 1
#     if flip == "yazi":
#         yazi += 1
#     elif flip == "tura":
#         tura += 1

# sentence = input("Give me a sentence: ")
# words = sentence.split()
# counter = 0
# longest = 0

# while counter < len(words):
#     if len(words[counter]) < len(words):
#         longest = len(words[counter])
#     counter += 1
# print(f"the length of the longest word: {longest}")


# liste = [1, 2, 3, 4, 5]
# for i in liste:
#     print(i)


# seasons = ["spring", "summer", "autumn", "winter"]
# seasons1 = set(seasons)

# for i in seasons1:
#     print(i)




# names = ["Ahmet", "Ayse", "Adam", "Joseph", "Gabriel"]

# for i in names:
#     print(f"Hello {i}")



# liste = []
# for i in range(1, 6):
#     liste.append(i)
# print(liste)



# word = "Clarusway"
# count = 0
# for i in word:
#     count += 1
#     if count < len(word):
#         i = i + "-"
#     print(i, end="")


# print('abcdefcdghcd'.split('cd'))