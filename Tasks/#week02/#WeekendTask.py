# --------------------------------------------WEEKEND TASK is completed--------------------------------------------
import random

name_1 = input('Birinci oyuncunun adi :')
name_2 = input('Ikinci oyuncunun adi :')

print(f"Hormetli {name_1} ve {name_2} ")
print("Her birinizin 5 cehd etme shansiniz var.Her duzgun texmin size 1 xal qazandiracaq. Ugurlar!")

name_1_total = 0
name_2_total = 0
xal = 1

x = 1
while (x < 6):
    number = random.randint(1, 5)

    while(True):
        name_1_guess = int(input("Enter your guess : "))

        if name_1_guess == number:
            name_1_total += xal
            print("------------------------------")
            print(f"1 point was added to you {name_1} !")
            print("------------------------------")

        elif name_1_guess != number:
            print(f"Sorry {name_1}, your guess is False")

        break

    while(True):
        name_2_guess = int(input("Enter your guess : "))

        if name_2_guess == number:
            name_2_total += xal
            print("------------------------------")
            print(f"1 point was added to you {name_2} !")
            print("------------------------------")

        elif name_2_guess != number:
            print(f"Sorry {name_2}, your guess is false")

        break

    x += 1


if name_1_total > name_2_total:
    print(f"{name_1}, you WIN!!!")
    print(f"{name_1}, your total point is {name_1_total}")

elif name_1_total < name_2_total:
    print(f"{name_2}, you WIN!!!")
    print(f"{name_2}, your total point is {name_2_total}")


else:
    print(f"{name_1} and {name_2} your point is equal")

