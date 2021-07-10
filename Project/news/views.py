from django.shortcuts import render
from .models import *
# Create your views here.
def news(request):
    news = News.objects.all()
    context = {
        'news' : news
    }
    return render(request,'news.html',context)

def news_detail(request, slug):
    news = News.objects.get(slug=slug)
    return render(request, "news-detail.html" , {'news' : news})