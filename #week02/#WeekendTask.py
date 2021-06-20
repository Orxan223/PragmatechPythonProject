#----------------------------------------------------Game Task-------------------------------------------------


# ------------------------------------------------ HELE TAMAMLANMAYIB
import random


number = random.randint(1, 5)
print(number)
list = [1, 2, 3, 4, 5]

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
x=1
while(x<6):


    while (True):
        guess_1 = int(input("player_1 Eded daxil edin :"))
        guess_1 = int(guess_1)
        if guess_1 != number_of_guesses:
            print(f"{player_1} sefdir")
        else:  
            print("False")
        break

    if guess_1 == number_of_guesses:
        print(f'{player_1} tebrikler')
        player_1.append(xal)
        print(f"player_1 sizin xaliniz{xal} ")



    while (True):
        guess_2 = int(input("player_2 Eded daxil edin :"))
        guess_2 = int(guess_2)

        if guess_2 != number_of_guesses:
            print(f"{player_2} sefdir")

        else:
            print("False")
        break


    if guess_2 == number_of_guesses:
        print(f'{player_2} tebrikler')
        player_2.append(xal)
        print(f"player_2 sizin xaliniz{xal} ")
            

for x in player_1:
    total_player_2 = total_player_1 + x
print(f"{player_1} xaliniz :")


for y in player_2:
    total_player_2 = total_player_2 + y
print(f"{player_2} xaliniz :")

if total_player_1 > total_player_2:
    print("Tebrikler siz qalibsiniz")


if total_player_1 < total_player_2:
    print("Tebrikler siz qalibsiniz")


else:
    print("Sizin xallar beraberdir")
