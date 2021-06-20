#----------------------------------------------------Game Task-------------------------------------------------


# ------------------------------------------------ HELE TAMAMLANMAYIB
# import random

# name = input('Birinci oyuncunun adi :')
# nameX = input('Ikinci oyuncunun adi :')
# print(f"Hormetli {name} ve {nameX} ")
# print("Her birinizin 5 cehd etme shansiniz var.Her duzgun texmin size 1 xal qazandiracaq. Ugurlar")

# number = random.randint(1,5)
# guess = 0


# while number != guess:
#     guess = input("1 ve 5 arasinda reqem texmin edin :")
#     guess = int(guess)

#     if number == guess:
#         print("Tebrikler")
#         break

#     else:
#         print("Təəssüf , yeniden cehd edin ")



import random


number = random.randint(1, 10)

player_1 = []
player_2 = []
xal = []

number_of_guesses = 0

total_player_1 = 0
total_player_2 = 0


player_1 = input('Birinci oyuncunun adi :')
player_2 = input('Ikinci oyuncunun adi :')
print(f"Hormetli {player_1} ve {player_2} ")
print("Her birinizin 5 cehd etme shansiniz var.Her duzgun texmin size 1 xal qazandiracaq. Ugurlar!")

while number_of_guesses < 5:
    guess = int(input())
    guess = int(guess)
    if guess != number:
        print(f"{player_1} sefdir")
    elif guess == number:
        print(f'{player_1} tebrikler')
        player_1.append(xal)
    else:
        print("Teessuf")
    break

while number_of_guesses < 5:
    tex = int(input())
    tex = int(guess)
    if guess != number:
        print(f"{player_2} sefdir")
    elif guess == number:
        print(f'{player_2} tebrikler')
        player_2.append(xal)
    else:
        print("Teessuf")
    break

for x in player_1:
    x += total_player_1
print(f"{player_1} xaliniz :")


for x in player_2:
    x += total_player_2
print(f"{player_2} xaliniz :")

if player_1 > player_2:
    print("Tebrikler siz qalibsiniz")


if player_1 < player_2:
    print("Tebrikler siz qalibsiniz")


else:
    print("Sizin xallar beraberdir")
