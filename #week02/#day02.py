#------------------------------------------------STATIC METHODS-----------------------------------------
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
#---------Class.staticmethodFunc()
#                     or
#         Class().staticmethodFunc()


#------------------------------------------------Ne vaxd static methods istifade edirik?----------------------
# Statik metodların məhdud istifadə vəziyyəti var, 
# çünki sinif metodları və ya bir sinif daxilində olan digər metodlar kimi,
# sinifin öz xüsusiyyətlərinə daxil ola bilmirlər.

# Bir sinifin hər hansı bir xüsusiyyətinə çatmayan, 
# lakin onun sinifə aid olduğu mənasını verən bir yardım proqramına ehtiyacınız olduqda,
# statik funksiyalardan istifadə edirik.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    #Class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
       
    @staticmethod
    def isAdult(age):
        return age > 18
   
person1 = Person('orxan', 22)
person2 = Person.fromBirthYear('mayank', 1997)
   
print (person1.age)
print (person2.age)
   
# print the result
print (Person.isAdult(22))