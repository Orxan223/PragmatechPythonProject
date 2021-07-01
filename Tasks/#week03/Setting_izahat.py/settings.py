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