from django.shortcuts import render
from .models import About, Choose
# Create your views here.


def index(request):
    about = About.objects.all()
    choose = Choose.objects.all()
    context = {
        "about" : about,
        'choose' : choose
    }
    return render(request, "index.html",context)


def blog(request):
    return render(request, "blog.html")


def about(request):
    # about = About.objects.all()
    # context = {
    #     'about' :about
    # }
    return render(request, "about.html")


def technology(request):
    return render(request, "technology.html")


def case(request):
    return render(request, "case.html")


def team(request):
    return render(request, "team.html")


def counter(request):
    return render(request, "counter.html")


def skills(request):
    return render(request, "skills.html")


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
