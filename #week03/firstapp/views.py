from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")


def about(request):
    return render(request, "about.html")

def technology(request):
    return render(request, "technology.html")

def case(request):
    return render(request, "case.html")



def counter(request):
    return render(request, "counter.html")



def news(request):
    return render(request, "news.html")



def work(request):
    return render(request, "work.html")





def skills(request):
    return render(request, "skills.html")


def team(request):
    return render(request, "team.html")



def choose(request):
    return render(request, "choose.html")


def contact(request):
    return render(request, "contact.html")
