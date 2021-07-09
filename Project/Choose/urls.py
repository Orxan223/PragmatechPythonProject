from django.contrib import admin
from django.urls import path,include
from .views import choose
app_name = 'choose'

urlpatterns = [
    path('', choose , name='choose'),
]

