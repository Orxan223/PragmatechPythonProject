from django.shortcuts import render
from .models import Team

def team(request):
    team = Team.objects.all()
    
    context = {
        "team" : team,
    }
    return render(request, "team.html",context)
 