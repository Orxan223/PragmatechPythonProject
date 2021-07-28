from django.http import request
from django.shortcuts import render,redirect
from .models import About, Choose,Skill,Blog,Contact
from django.forms import forms
from .forms import  ContactForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import TemplateView



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




from django.shortcuts import render
from django.views.generic import TemplateView


class CounterView(TemplateView):
    template_name = 'counter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_work'] = Work.objects.count()
        return context


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






def like_recipe(request):
    if request.method == 'POST' :
        liked_recipes = request.COOKIES.get("liked_recipes" , "")
        recipe_id = request.POST.get('recipe_id')

    html = render_to_string('successfuly_liked.html')
    response = HttpResponse(html)
    response.set_cookie('liked_recipes' , f'{liked_recipes}{recipe_id},' )
    return response