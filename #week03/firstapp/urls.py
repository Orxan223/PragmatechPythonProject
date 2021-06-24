from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/',blog),
    path('about/',about),
    path('case/',case),
    path('choose/',choose),
    path('counter/',counter),
    path('news/',news),
    path('service/',service),
    path('skills/',skills),
    path('team/',team),
    path('work/',work),
]
