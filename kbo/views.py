from django.shortcuts import render, get_object_or_404
from .models import TeamList, Hitting, Pitcher

# Create your views here.
def index(request):
    team = TeamList.objects.all().order_by('rank')
    update = TeamList.objects.all()[:1]
    team_data = {
        'team':team,
        'update':update,
    }

    return render(request, 'kbo/index.html', team_data)

def team_detail(request,team):
    
    aa = TeamList.objects.get(team=team)


    player_h = Hitting.objects.filter(team=aa)
    player_p = Pitcher.objects.filter(team=aa)
    player_t = Pitcher.objects.filter(team=aa)[:1]
    
    detail = {
        'aa':aa,
        'player_h':player_h,
        'player_p':player_p,
        'player_t':player_t,
    }

    return render(request, 'kbo/team_detail.html',detail)


def team_info(request,team):
    info = TeamList.objects.filter(team=team)
    
    info_detail = {
        'info':info
    }

    return render(request, 'kbo/team_info.html', info_detail)

