from django.shortcuts import render
from .models import TeamList

# Create your views here.
def index(request):
    team = TeamList.objects.all()


    return render(request, 'kbo/index.html', {'team':team})