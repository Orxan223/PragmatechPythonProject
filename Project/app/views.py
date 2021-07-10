from django.http import request
from django.shortcuts import render,redirect
from .models import About, Choose,Skill,Blog,Contact
# Create your views here.
from django.forms import forms
from .forms import  ContactForm
from django.contrib import messages


def index(request):
    about = About.objects.all()
    choose = Choose.objects.all()
    skill = Skill.objects.all()
    blog = Blog.objects.all()
 
    form=ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            form = Contact(full_name=full_name,email=email, subject=subject, message=message)
            form.save()
            messages.success(request, 'Mesaj gonderildi...')

            return redirect ('index')
    context = {
        "about" : about,
        'choose' : choose,
        'skill' : skill,
        'blog' : blog,
        'form' : form,
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




def team(request):
    return render(request, "team.html")


def choose(request):
    return render(request, "choose.html")


def contact(request):
    return render(request, "contact.html")






