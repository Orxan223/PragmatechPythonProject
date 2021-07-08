from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),

    path('blog/', blog, name='blog'),

    path('technology/',technology,name='technology'),

    path('about/',about,name='about'),

    path('case/',case,name='case'),

    path('work/',work,name='work'),

    
    path('skills/',skills,name='skills'),

    path('news/',news,name='news'),




    path('news-detail/',news_detail,name='news-detail'),


    path('counter/',counter,name='counter'),





    path('team/',team,name='team'),

     path('choose/',choose,name='choose'),


     path('contact/',contact,name='contact'),



]
