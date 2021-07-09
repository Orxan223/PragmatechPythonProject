from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index, name='index'),

    path('blog/', blog, name='blog'),





    
    path('skill/',skill,name='skill'),

    path('news/',news,name='news'),


    path('news-detail/',news_detail,name='news-detail'),


    path('counter/',counter,name='counter'),



    path('team/', include('Team.urls')),


    path('choose/',include('Choose.urls')),


    path('work/',include('work.urls')),

    path('work/',work,name='work'),

    path('team/',team,name='team'),

    path('choose/',choose,name='choose'),


    path('contact/',contact,name='contact'),
]
