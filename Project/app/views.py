from django.shortcuts import render
from .models import About, Choose,Skill,Blog,News
# Create your views here.


def index(request):
    about = About.objects.all()
    choose = Choose.objects.all()
    skill = Skill.objects.all()
    blog = Blog.objects.all()
    news = News.objects.all()
    context = {
        "about" : about,
        'choose' : choose,
        'skill' : skill,
        'blog' : blog,
        'news' : news,

    }
    return render(request, "index.html",context)


def blog(request):
    return render(request, "blog.html")







def counter(request):
    return render(request, "counter.html")


def skill(request):
    return render(request, "skill.html")


def news(request):
    return render(request, "news.html")


def work(request):
    return render(request, "work.html")


def news_detail(request):
    return render(request, "news-detail.html")


def team(request):
    return render(request, "team.html")


def choose(request):
    return render(request, "choose.html")


def contact(request):
    return render(request, "contact.html")
