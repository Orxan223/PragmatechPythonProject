# Task01.day
import random
import math


# 1)
from typing import Counter


x = 'Salam'
print(x)

# 2)
a = "orxan"
b = "salmanov"

d = a.capitalize()
c = b.capitalize()

print (d + ' ' + c)

# 3)
print('Yevlax','Kurdemir','Berde', 'Terter', sep='*')

# 4)
a = ' Macaristan'[::-1]
print(a)

# 5)
print('Languages : Python C JavaScript')

# 6)
print(' “Forever for now” is one of the')
print(" “Forever for now” \n is one of the")
print(" “Forever for now” \t is one of the")
print(" “Forever for now” \bis one of the")

# 7)
a = ( "O, ümumi PFA və FWA mükafatını alan ilk futbolçu oldu. 2008,2013,2014,2016-cü illərdə Qızıl top mükafatını qazandı")
print(len(a))
a = "O, ümumi PFA və FWA mükafatını alan ilk futbolçu oldu. 2008,2013,2014,2016-cü illərdə Qızıl top mükafatını qazandı"
print(a[:57])

# 8)
a = 3
b = 4
print (f" {a} ustu 4 = {a**4}, {b} ustu 3 ise {b**3}")

# 9)
x = 10
y = 55
print(x > y and x < y )

# 10)
a ='Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function". Orwell like Marcel Proust fears that the habit of conforming to the force benumbs sensations and erases the perception of the world. Technological totalitarianism alienates senses, controls human behaviour and leads to linguistic degradation'
word = 'does '

if word in a:
    print("True")
else:
    print("False")


# 11)
a = round(5.567, 2)
print(a)

# 12)


# 13)
c = random.randrange(1,8)
print (math.sqrt(c))