from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class NewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news-detail.html'
    context_object_name = 'news'