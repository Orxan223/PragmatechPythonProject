# --------------------------------------------------Class-----------------------------------------------------

#  Bir masin fikirlesek . Bu masinin rengi , motor gucu,qapi sayisi ve s. kimi ozelikleri(deyisken) var. Birde motoru isletmek ,
#  qapilari kilitlemek kimi davranislari(method) var. Bunlar ele masinin butun ozeliklerini ve methodlarini eks
# etdiren class-in olusdurulmasidir.

# --------------------------------------------------Object-----------------------------------------------------

# Tutaq ki , bina tikilir ve bu binani erseye getirmek ucun bir plan ortaya qoyulur .Sonra bu plan esasinda 
# bina tikilmeye baslayir . Hemin bu plani class-dir , plan uzerinden tikilen bina ise objectdir.
# Ayrica biz bu planlar uzerinden bir nece dene de bina tike bilerik . Bu ise o demekdir ki, 
# bir classin bir nece dene object-i ola biler.





veriable = 10                          # variable

def function(b):                       # function  
    return b ** 2

class C:

    c = 20                      # class attribute

    def __init__(self, d):      # "dunder" method
        self.d = d              # instance attribute

    def show(self):             # method
        print(self.c, self.d) 

e = C(30)
e.d = 40
e.show()                        # another instance variable