import random

user_1 = input("Ilk oyuncunu daxil edin: ")
user_2 = input("Ikinci oyuncunu daxil edin: ")

user_1_xal=0
user_2_xal=0
xal=1

i=0

while(i<5):
    reqem=random.randint(1,5)
    print("---------------------------------------------")
    print("Tapilmali eded: ", reqem)
    print("--------------------")
    while(True):
        user_1_reqem = int(input(f"{user_1} Eded daxil edin: "))
        if user_1_reqem == reqem:
            user_1_xal += xal
        break
    while(True):
        user_2_reqem = int(input(f"{user_2} Eded daxil edin:"))
        if user_2_reqem == reqem:
            user_2_xal += xal
        break
    i+=1

print("---------------------------------------------")
print(user_1, "- Toplam",  user_1_xal, "xaliniz var")
print(user_2, "- Toplam",  user_2_xal, "xaliniz var")
print("---------------------------------------------")
if user_1_xal > user_2_xal:
    print(user_1, "-- SIZ QALIBSIZ")
elif user_1_xal < user_2_xal:
    print(user_2, "-- SIZ QALINSIZ")
else:
    print("---------------------------------------------")
    print("BERABERE QALDINIZ") 