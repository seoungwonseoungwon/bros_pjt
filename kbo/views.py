from django.shortcuts import render, get_object_or_404
from .models import TeamList, Hitting, Pitcher

# Create your views here.
def index(request):
    team = TeamList.objects.all()


    return render(request, 'kbo/index.html', {'team':team})

def team_detail(request,pk):
    aa = TeamList.objects.get(pk=pk)
    


    return render(request, 'kbo/team_detail.html',{'aa':aa})
# def team_detail(request,pk):
#     # player_h = Hitting.objects.get(team_id=team_id)
#     team_obj = get_object_or_404(TeamList, team=pk)
#     hitter = Hitting.objects.filter(team=team_obj)
#     pitcher = Pitcher.objects.filter(team=team_obj)
#     # print(player_h)
#     # player_p = Pitcher.objects.get(team_id=team_id)
#     player = {
#         'team':team_obj,
#         'hitter' : hitter,
#         'pitcher': pitcher
#     }


#     return render(request, 'kbo/team_detail.html',player)