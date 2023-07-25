import csv
# from mydb_env import *
# import pymysql
# from emoji import core
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bros_kbo_pjt.settings")
django.setup()

# from company_info.models import Company_list
from kbo.models import TeamPlayer, TeamList

f = open('data/타자/2023samsung_hitting.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr)
# name 1
# team 2
# war 3
# games_played 4
# hits 8
# home_runs 11
# batting_average 23
# on_base_plus_slugging  26

for i in rdr:
    # if i[1] == '문상인':
    #     i[23] = 0
    #     i[26] = 0

    TeamPlayer.objects.create(
        name = i[1],
        war = i[3],
        hits = i[8],
        home_runs = i[11],
        batting_average = i[23],
        on_base_plus_slugging = i[26],
        games_played = i[4],
        position = '타자',
        # team = 1
    )
