# 1)
a = [55, 42, 33, 27, 76,95]
cem = 0
for x in a:
    cem += x
print(cem)

# 2)
list = [55, 99, 33, 27, 77]
i = list[0]
for x in list:
    if x > i:
        i = x

print('En boyuk eded :', i)

# 3)
list = [55 , 42 , 13 , 27 , 1]
i = list[0]
for x in list:
    if x < i:
        i = x

print('En kicik eded :', i)

# 4)
# list =  ['abc', 'xyz', 'aba', '1221','4554']
# a = 0
# for x in list:
#     if len(x) >  x[0] == x[-1]: #2and
#         a += 1

# print(a)


# 5)
l = []
if not l:
    print("List is empty")

#6)
# my_text = "Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings"
# a = my_text.split

# 7)
list = [55, 42, 33, 27, 78]
i = []
for x in list:
    if x % 2 == 1:
        i.append(x)
print(i)


