from django.shortcuts import render
from .models import TeamList, Hitting

# Create your views here.
def index(request):
    team = TeamList.objects.all()


    return render(request, 'kbo/index.html', {'team':team})

def team_detail(request):
    player = Hitting.objects.all()

    return render(request, 'kbo/team_datil.html', {'player':player})