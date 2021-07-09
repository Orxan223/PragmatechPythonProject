from django.shortcuts import render
from .models import Choose
# Create your views here.
def choose(request):
    choose = Choose.objects.all()
    context = {
        'choose' : choose
    }
    return render (request, 'choose.html',context)