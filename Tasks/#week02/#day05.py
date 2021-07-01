#-----------------------------------------------Abstract--------------------------------------------------- 

from abc import ABC, abstractmethod


class Coxbucaqli(ABC):

    @abstractmethod
    def teref(self):
        pass


class Ucbucaq(Coxbucaqli):

    # overriding abstract method
    def teref(self):
        print("I have 3 sides")


class beşbucaq(Coxbucaqli):

    def teref(self):
        print("I have 5 sides")


class Altıbucaq(Coxbucaqli):

    def teref(self):
        print("I have 6 sides")


class Dördbucaqlı(Coxbucaqli):

    def teref(self):
        print("I have 4 sides")


R = Ucbucaq()
R.teref()

K = beşbucaq()
K.teref()

R = Altıbucaq()
R.teref()

K = Dördbucaqlı()
K.teref()


# -------------------------------------------------Netice-------------------------------------------------

# --------------Abstrakt dərslərdən nə vaxt istifadə edecik?

# -Kodu bir-birinə yaxın olan bir neçə sinif arasında bölüşmək üçün mücərrəd dərslərdən istifadə edirik.

# -Proyekte baslayandan ,evvel saytda bu hisseler olmalidi deyerek plan qururuq,
# abstrakt bu zaman hemin planlari unudanda bize xatirladir(remind).

# -Abstrakt siniflər, nümunə qura bilməyəcəyiniz siniflərdir. Yeni obyekt acmaq olmmur Abstrakt-dan.
# -Abstrakt sinifləri təyin etmək üçün abc modulundan istifadə edirik.


# ---------------------------------------------- Encapsulation----------------------------------------------
class A:
    def __init__(self, x=10, y=6):
        self.__x = x
        self._y = y


obj = A()
print(obj._y) #protected
print(obj._A__x) #private normal erismek mumkun olmadigi ucun bele yazilir. Normal qayda da erismek
#                isdedikde ise setter , getter istifade edilir

# Bunun sebebi :
# class = protected
# obj = private
# class = protected + obj = private
# Yeni _A__x


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def display(self):
        return (self.name)

    def getAge(self):
        return (self.__age)

    def setAge(self, age):
        self.__age = age

    


person = Person('Dev', 30)

print(person.display())

person.setAge(35)
print(person.getAge())

# ---------------------------------------------- Encapsulation Ustun cehetleri----------------------------------------------

# Tətbiqlər etibarlı şəkildə saxlanıla bilər.
# Kodun oxunaqlılığını artırır. Kodun bir hissəsindəki dəyişikliklər digərini narahat etməyəcəkdir.
# Kapsulasiya məlumatların qorunmasını təmin edir və təsadüfən məlumatların əldə edilməsinin qarşısını alır.
