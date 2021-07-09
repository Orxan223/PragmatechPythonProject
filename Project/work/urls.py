from django.urls import path
from .views import *

app_name = 'work'

urlpatterns = [
    path('',work,name='work'),
]