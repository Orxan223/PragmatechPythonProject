from django.urls import path, include
from .views import NewsListView , NewsDetailView



urlpatterns = [
    path('',NewsListView.as_view(),name='news'),
    path('<slug:slug>',NewsDetailView.as_view(),name='news_detail'),
]