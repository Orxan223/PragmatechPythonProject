# ------------------------------------------------STATIC METHODS-----------------------------------------
# class MyClass:
#     def method(self):
#         return 'instance method called', self

#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls

#     @staticmethod
#     def staticmethod():
#         return 'static method called'


# Statik metodlar, class metodları kimi, bir obyekt üçün deyil, bir classla bağlı olan metodlardır.


# Statik metodla class metodu arasındakı fərq:

# Statik metod sinif haqqında heç bir şey bilmir və yalnız parametrlərlə məşğul olur.
# Həm class, həm də obyekt tərəfindən adlandırıla bilər.
# ---------Class.staticmethodFunc()
#                     or
#         Class().staticmethodFunc()


# ------------------------------------------------Ne vaxd static methods istifade edirik?----------------------
# Statik metodların məhdud istifadə vəziyyəti var,
# çünki sinif metodları və ya bir sinif daxilində olan digər metodlar kimi,
# sinifin öz xüsusiyyətlərinə daxil ola bilmirlər.

# Bir sinifin hər hansı bir xüsusiyyətinə çatmayan,
# lakin onun sinifə aid olduğu mənasını verən bir yardım proqramına ehtiyacınız olduqda,
# statik funksiyalardan istifadə edirik.
# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     #Class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)

#     @staticmethod
#     def isAdult(age):
#         return age > 18

# person1 = Person('orxan', 22)
# person2 = Person.fromBirthYear('mayank', 1997)

# print (person1.age)
# print (person2.age)

# # print the result
# print (Person.isAdult(22))

# -----------------------------------------------------DUNDER METHOD--------------------------------------

# 1)---------------       __add__()
num = 10

print(num.__add__(5))


# 2)----------------     __str__()


num = 12
print(str(num))
# yuxaridaki numune ile asagidaki eynidir
print(int.__str__(num))


# 3)----------------     __init__()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Orxan", 53)

print(p1.name)
print(p1.age)


# 4)----------------       __len__()

nums = [1, 2, 3, 4, 5]
print(len(nums))
# yuxaridaki numune ile asagidaki eynidir
print(nums.__len__())

# 5)-------------------    __getattr__()


class Dummy(object):
    def __getattr__(self, attr):
        return attr.upper()


d = Dummy()
print(d.does_not_exist)
print(d.what_about_this_one)

# 6)--------------------    __dict__()


class Car:
    def __init__(self, marka, color):
        self.marka = marka
        self.color = color


cr = Car('BMW', 'Black')
print(cr.__dict__)

# 7)---------------------     __setattr__


class School:
    def __setattr__(self, name, value):
        self.__dict__[name] = value.upper()


f = School()
f.student = "student"
print(f.student)

# 8)----------------------     __abs__ 
v = -1
v.__abs__()
print(abs(v))

# 9)----------------------     __dir__
class Nese:
    def __init__(self, x):
        self.x = x

print(dir(Nese))

# class Person:

#     def __init__(self, person_name, person_age):
#         self.name = person_name
#         self.age = person_age

#     def __str__(self):
#         return f'Person name is {self.name} and age is {self.age}'

#     def __repr__(self):
#         return f'Person(name={self.name}, age={self.age})'


# p = Person('Pankaj', 34)

# print(p.__str__())
# print(p.__repr__())


# class MyClass:
#     x = 0
#     y = ""

#     def __init__(self, anyNumber, anyString):
#         self.x = anyNumber
#         self.y = anyString
#     def __repr__ (self):
#         return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'


# myObject = MyClass(12345, "Hello")

# print(myObject.__str__())
# print(myObject)
# print(str(myObject))
# print(myObject.__repr__())
