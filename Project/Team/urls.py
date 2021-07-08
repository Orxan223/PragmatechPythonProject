from django.urls import path
from .views import *


urlpatterns = [
    path('team/',team,name='team'),
]