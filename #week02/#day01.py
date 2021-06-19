#-----------------------------------------------Polimorfizm-------------------------------------------- 

class Animal:
    def introduction(self):
        print("there are many types animal")

    def wild(self):
        print("some animals wild but some not")


class Cat(Animal):
    def wild(self):
        print("Cat is not wild")


class Leon(Animal):
    def wild(self):
        print("Leon is wild")


a = Animal()
b = Cat()
c = Leon()

a.introduction()
a.wild()

b.introduction()
b.wild()


c.introduction()
c.wild()


# --------------------------------------------------------- SUPER()
# Bir class ne vaxd ki, diger class-in ozeliklerine erismek isdiyende super() istifade edirik
class Parent:
    def __init__(self, a):
        self.a = a

    def printmessage(self):
        print(self.a)


class Child(Parent):
    def __init__(self, a):
        super().__init__(a)


x = Child("Hello, and welcome!")

x.printmessage()
