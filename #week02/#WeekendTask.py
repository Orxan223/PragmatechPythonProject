# --- HELE TAMAMLANMAYIB


import random

name = input()
nameX = input()

number = random.randint(1,5)
guess = 0


while number != guess:
    guess = input("1 ve 5 arasinda reqem texmin edin :")
    guess = int(guess)

    if number == guess:
        print("Tebrikler")
        break

    else:
        print("Təəssüf , yeniden cehd edin ")