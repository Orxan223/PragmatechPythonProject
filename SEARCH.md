<!-- # --------------------------------------------------Class-----------------------------------------------------

#  Bir masin fikirlesek . Bu masinin rengi , motor gucu,qapi sayisi ve s. kimi ozelikleri(deyisken) var. Birde motoru isletmek ,
#  qapilari kilitlemek kimi davranislari(method) var. Bunlar ele masinin butun ozeliklerini ve methodlarini eks
# etdiren class-in olusdurulmasidir.

# --------------------------------------------------Object-----------------------------------------------------

# Tutaq ki , bina tikilir ve bu binani erseye getirmek ucun bir plan ortaya qoyulur .Sonra bu plan esasinda 
# bina tikilmeye baslayir . Hemin bu plani class-dir , plan uzerinden tikilen bina ise objectdir.
# Ayrica biz bu planlar uzerinden bir nece dene de bina tike bilerik . Bu ise o demekdir ki, 
# bir classin bir nece dene object-i ola biler. -->

<!-- # ------------------------------------------------STATIC METHODS-----------------------------------------
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

# Statik metod class haqqında heç bir şey bilmir və yalnız parametrlərlə məşğul olur.
# Həm class, həm də obyekt tərəfindən adlandırıla bilər.
# ---------Class.staticmethodFunc()
#                     or
#         Class().staticmethodFunc()


# ------------------------------------------------Ne vaxd static methods istifade edirik?----------------------
# Statik metodların məhdud istifadə vəziyyəti var,
# çünki class metodları və ya bir class daxilində olan digər metodlar kimi,
# class-in öz xüsusiyyətlərinə daxil ola bilmirlər.

# Bir claass-in hər hansı bir xüsusiyyətine çatmayan,
# lakin onun class-a aid olduğu mənasını veren bir yardım proqramına ehtiyacınız olduqda,
# statik funksiyalardan istifadə edirik. -->

<!-- #-----------------------------------------------Abstract--------------------------------------------------- 

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


# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# # ---Proyektin hansi direction(istiqamet)-da yerlesdiyini gosderir



# SECRET_KEY = 'django-insecure-y4%%m0m$hq%!b3s@@^gih7yt1!+k3c9bs$lc-0cd_)(panw9qa'
# #-------Sayt hazir product oldugu zaman ,bunu hamidan gizli saxlamaq lazimdir,ve secret key hemin bu tehlukesizlik
#  ucundur------- 



# DEBUG = True
# # ------Erorlari gosterir etrafli sekilde ve belece erorun yerini rahatliqla tapa bilirik.


# ALLOWED_HOSTS = []
# # HTTP Host başlığı hücumlarının qarşısını almaq üçün bir təhlukesizlik tedbiridir.
# Esasen servere yerlesdirerken komeymize catir

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'look'
# ]
# # ACdiqimiz app-lari burda qeyd edirik

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# #------Geden request ,gelen respond MIDDLEWARE ile tenzimlenir. Bir nov filterleme kimi



# ROOT_URLCONF = 'Site.urls'
# # Proyektin adi ve icerisindeki urls.py gosderir

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': ['templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
# #------Bizim html-ri mehs burda yerlesdiririk. Templates acan zaman DIRS-de 'templates' seklinde qeyd etmek lazimdir
# #------Optins,view gondermeden jinja istifade edir. App ve ya views gondermirik,contextde olur ( context_processors.debug, 
# # context_processors.request )

# WSGI_APPLICATION = 'Site.wsgi.application'
# #Isdediyimiz portu veririk ve ora gedir.
# #Daha etrafli gelecek derslerde tanis olaciq,basa dusmeden nese yazmaq isdemirem(Mellim qeyd etdi gelecek derslerde
# kececik)



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# # -------DATABASES uzerinde default olaraq gelen sqlite-dir. Lakin bizim isdeyimize gore bunu deyisdire bilerik

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# # -----Kodlarin guvenliyi baximindan bizim komeyimize yetir.
# # -----Meselen , minimum uzunlugu ve yaxud butun kodun reqemlerden ibaret oldugu zaman ,bize xeberdarliq olaraq 
# # bildirilir ki, kodunuz guvenli deyil.


# # LANGUAGE_CODE = 'en-us'

# # TIME_ZONE = 'UTC'

# # USE_I18N = True

# # USE_L10N = True

# # USE_TZ = True

# #-------Vaxdlarimizi burdan isdediymiz kimi deyise bilerik.Meselen vaxdi ingilterenin deyilde Azerbaycana
# #-------uygun hesablanmasini isdiye bilerik ve onu gelib burda oz deyisikliklerimizi etmeliyik.


# STATIC_URL = '/static/'

# Turaq ki bizim saytin sekilerin istifade edirler amma biz istemirik etsinler,
# ona gore butun sekilerin yerini deyismek evezine burda deyisirik ve isdeyimizr nail oluruq
# ISdediyimiz adi qoya bilerik tehlukesizlik ucun. Meselen STATIC_URL = '/wefwfwefwe/'




<!-- -----------------------------------------------Model------------------------------------------------------

                        <!-- Media -->
<!-- Site/urls:
from django.conf import settings
from django.conf.urls.static import static

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Site/settings:
STATIC_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



Filds:
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)



Class Meta:
    ordering = ('title', '-created_at')



Relations:
A)1 yazicinin coxlu kitabi olar biler(one to many)

ForeignKey cox terefe verilir ,yeni hansi hansindan aslidir. Kitab yazicidan asili deyil.
ForeignKey asli terefde olur.
ForeignKey verende foreignKey vereceymiz teref cox teref olmalidir.



B)coxlu Receipe  1 Category(one to many):
a Category-de 10 dene Receipe ola biler.

COX TEREF HARDADIRSA RELATIONS ORA VERILIR. --> 