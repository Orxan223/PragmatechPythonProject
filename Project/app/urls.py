from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('team/', include('Team.urls')),
    path('choose/', include('Choose.urls')),
    path('work/', include('work.urls')),
    path('news/',include('news.urls')),
    path('news/', news, name='news'),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('skill/', skill, name='skill'),
    path('work/', work, name='work'),
    path('team/', team, name='team'),
    path('choose/', choose, name='choose'),
    path('contact/', contact, name='contact'),
    path('like/', like_recipe, name='like'),
    path('counter/', CounterView.as_view(), name="counter"),


]
