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


