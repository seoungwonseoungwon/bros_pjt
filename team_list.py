import csv
# from mydb_env import *
# import pymysql
# from emoji import core
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bros_kbo_pjt.settings")
django.setup()

# from company_info.models import Company_list
from kbo.models import Pitcher, TeamList

f = open('data/투수/23NC_pitching__records.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
# next(rdr)
# name 1
# team 2
# war 3
# games_played 4
# wins 8
# losses 9
# era  26 
# saves 10
# holds 11
# innings_pitched 12
# print(team_instance)




for i in rdr:

    # print(i[1],i[2])
    # 팀 이름 가져오기
    team_name = i[2]

    try:
        # 해당 팀의 TeamList 모델 객체 가져오기
        team_instance = TeamList.objects.get(team=team_name)
    except TeamList.DoesNotExist:
        # Handle the case when the team doesn't exist in TeamList
        # For example, you may want to create the team or handle it differently.
        continue
    if i[1] == '문경찬':
        i[26] = 0
            
    # Pitcher 모델에 데이터 저장
    Pitcher.objects.create(
        team=team_instance,
        name=i[1],
        war=float(i[3]),
        wins=int(i[8]),
        losses=int(i[9]),
        era=float(i[26]),
        games_played=int(i[4]),
        position='투수',
        saves = i[10],
        holds = i[11],
        innings_pitched = i[12],
    )




# f = open('data/투수/merged_pitching_records.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# next(rdr)
# # name 1
# # team 2
# # war 3
# # games_played 4
# # wins 8
# # losses 9
# # era  26 
# # print(team_instance)
# for i in rdr:
#     # print(i[26])
#     # break

#     Pitcher.objects.create(
#         team = '1',
#         name = i[1],
#         war = i[3],
#         wins = i[8],
#         losses = i[9],
#         era = i[26],
#         games_played = i[4],
#         position = '투수',
#     )
