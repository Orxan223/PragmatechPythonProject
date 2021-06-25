from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('blog/', blog, name='blog'),

    path('technology/',technology,name='technology'),

    path('about/',about,name='about'),

    path('case/',case,name='case'),

    path('work/',work,name='work'),

    path('team/',team,name='team'),
    
    path('skills/',skills,name='skills'),

    path('news/',news,name='news'),


    path('skills/',skills,name='skills'),


    path('counter/',counter,name='counter'),





    path('team/',team,name='team'),

     path('choose/',choose,name='choose'),


     path('contact/',contact,name='contact'),



]
