from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    data = {
        'team':teams,
    }
    return render(request, 'page/home.html', data)