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



<!-- -----------------------------------------------Admin------------------------------------------------------

    #list_display = ('title',)
    # Menasindan da gorunduyu kimi listdeki elemetleri display etmek ucundur

    # fields = ('title',)
    # Yalniz qeyd edilen hisseni gosderir

    # exclude = ('title',)
    # Qeyd edilen yer xaric , digerlerini gosderir

    # list_filter = ('text',) 
    # Admin sehifesinde sag hissede gorduyumuz filterleme isini gormek ucundur. Meselen
    # qeyd etdiyimiz kimi text gore filterleme etsek ,veridiyimiz textlere esasen filterleme isleri aparilacaq

    # search_fields = ('title',)
    # Admin page-de serach ucun yer acilir, ve burada qeyd etdiyimiz title gore seacrh edib bize getirir



<!-- -----------------------------------------------Form------------------------------------------------------
Form ustunlukleri:
-Daha tehlukesizdi
Html gore daha tehlukesizdi, cunki html qorumasi yoxdu amma formlarda csrf_token olduguna gore daha tehlukesizdi
-Coxlu funksiyalar var ,metodlar falan.Funksiyanaligi artirir.

----------------------------------------------------GET / POST-------------------------------------------------
GET - sehifeye kecid eden zaman yeni sehifenin url muraciet etdiyimiz zaman . Data uzunlugunda limitlemeler var.
Get - melumati elde elemek ,oxumaq

POST - sehifeden bize data gelirse. Daha tehlukesizdi
Post-neyise create elemekdir
Post- Data base melumat yazanda,submit kimi isler goren de 




-------------------------------------------------------Task---------------------------------------------

Aşağıdakı sualları cavablandıraraq kod nümumələri ilə izahlı şəkildə research.md faylına yazın
Template tag nədir?
Template filter nədir?


Template {% tag %} nədir?
Tamplate taglar kod təkrarlanmasını aradan qaldırmaq üçündur.Səhifəde davamlı göstərməli olduğunuz bir sahə var və bu sahənin göstərilməsi üçün göndərilən məlumatları hər səhifəyə yenidən göndərməlisiniz. Tamplate taglar  işə başladığı yer budur. Tamplate taglar , adından da göründüyü kimi, davamlı ehtiyac olduqda qısa etiketli bir tag çağırmaqdır.
Meselen :
Block -  Bildiyimiz block taglari var ki,bunu biz oz template-mizde istifade etmisik ve bunun da neticesidir ki,
biz daha az koddan istifade etmisik.
Csrf_token - biz tehlukesizlik vasitesile istifade edirik formlar-da



Template {{filter}} nədir?
Bize bezi funksionaliqlar vermkede komek olur. Bu kodlar vasitesile isdediymiz hiseleri filterliyerek en tez sekilde 
isdediyimiz neticeleri aliriq. Numunelerde bunun nece usdunluk verdiyine nezer yetirek (Algorithms) 


-------------------------------------------------------Docker---------------------------------------------
Docker nedir ?
- Butun emeliyyat sistemlerini uygunlasdirir.
:Meselen men neyise linuxda yaziram, sabah teamde bunu kimese versek ,hansiki windows isledir ,proyektimizi ona enivorement ile yox,docker file ile gonderecik. 
ve proyekt run olunanda o ounun emeliyyat sistemi ile islemiyecek dockerin icinden calisacaq.
-Virtual masinlardan daha suretli olur, 
-Izolyasiya olunmus yerdir ,hansiki orda muxtelif emeliyyat sistemlerine yazdigimiz kodlarin adaptasiya olumasi ucun istifade olunur.(Emrlerin tercume olunmasi kimi)


Dockerhub nedir ?
- orda imageler olur, framework kimi girib yukleyirik
Dockerden istifade edib emeliyat sistemimize windows yukleye bilerik(tam windows deyil),
onu hardan yukluyuruk dockerhubdan yukleriyirik .


Volume nedir ? 
- Docker yandirib sondurende , bizim melumatlar silinir(databaseden silinir) ve bizim 
value imkan verir ki, men gelib database sekil eleva eledim data elave eledim,
men komputeri sondurende dockerimde silinecek o sonende onun icindeki her sey silinir.Amma men o datalari saxlamaliyam
ona gore de value kodundan istifade edirik 


FROM python:3.9 - Dockere python getiririk

WORKDIR /code - bu folderi axdarir yoxdusa bele bir file acir

COPY . .  - kodlarimizi dockerin icerisine gondermeliyik

RUN pip install -r req.txt - hansii library istifade edib bilmediymize gore , onu req.txt(requirements.txt ) icinde gotururuk

ENV FLASK_APP=main.py = export  FLASK_APP=main.py 

VALUE = [ "./media","media_folder" ] - bura tutaqki sekil atiriq ve bunu copylarayiriq ,2cide file adidir

CMD [ "flask", "run" ]  - flusk run



-------------------------------------------------------Cookies---------------------------------------------
nedir?
-Fronend ve Backend-in goruse bileceyi yer  (elaqe qurmaq falan bundan istifade olunur).
Bir kart fikirles ,o kart vasitesile cofe alirsan gezirsen falan ,o kart senin vizan kimidir.Session id-de mehz
ele birseydir.Frontend sizin kodunuzu yox hemin session id olan kodu verir ve backend de gorurki heqiqeten bu adamin 
icazesi var.Yeni session id icazeni temin eden koddur.

