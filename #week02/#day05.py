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



# -------------------------------------------------Netice

# Abstrakt dərslərdən nə vaxt istifadə edecik?
# Kodu bir-birinə yaxın olan bir neçə sinif arasında bölüşmək üçün mücərrəd dərslərdən istifadə edirik. 


# -------------------------------------------------Xülasə
# Abstrakt siniflər, nümunə qura bilməyəcəyiniz siniflərdir. Yeni obyekt acmaq olmmur Abstrakt-dan.
# Abstrakt sinifləri təyin etmək üçün abc modulundan istifadə edirik.