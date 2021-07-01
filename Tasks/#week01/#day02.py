# 1)

a = int( input("Eded daxil edin :"))
b = int( input("Eded daxil edin :"))
c = int( input("Eded daxil edin :"))
d = int( input("Eded daxil edin :"))

if a == b == c == d:
    print(a ** 2) 
else:
    print((a+b+c+d))



# 2)
num = int(input("Ne qeder eded daxil edilsin :"))
list = []

for x in range(num):
    eded = int(input("Eded daxil edin: "))
    list.append(eded)

print("Boyuk eded:" , max(list))
print("Kicik eded: ", min(list))






# 3)
meyveler = {'alma' , 'armud' , 'banan'}
a = input("meyve adi daxil edin :")
if a in meyveler:
    print(a)
else:
    print('error')






# 4)
a = [55, 42, 33, 27, 76,95]
cem = 0
for x in a:
    cem += x
print(cem)

# 5)
list = [55, 99, 33, 27, 77]
i = list[0]
for x in list:
    if x > i:
        i = x

print('En boyuk eded :', i)

# 6)
list = [55 , 42 , 13 , 27 , 1]
i = list[0]
for x in list:
    if x < i:
        i = x

print('En kicik eded :', i)

# 7)
list =  ['abc', 'xyz', 'aba', '1221','4554']
a = 0
for x in list:
    if len(x) > 2 and  x[0] == x[-1]: 
        a += 1

print(a)


# 8)
l = []
if not l:
    print("List is empty")


# 9)
list = [55, 42, 33, 27, 78]
i = []
for x in list:
    if x % 2 == 1:
        i.append(x)
print(i)


