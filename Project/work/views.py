from django.shortcuts import render
from .models import Work
# Create your views here.
def work(request):
    work = Work.objects.all()
    context = {
        'work' : work
    }
    return render(request,'work.html',context)