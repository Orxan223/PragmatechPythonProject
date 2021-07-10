from django.urls import path, include
from .views import *


urlpatterns = [
    path('',news,name='news'),
    path('<slug:slug>',news_detail,name='news_detail'),
]