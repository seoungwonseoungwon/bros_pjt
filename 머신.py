import csv
import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bros_kbo_pjt.settings")
django.setup()

from kbo.models import PreRank, TeamList

f = open("data/머신머신.csv", "r", encoding='utf-8')
rdr = csv.reader(f)
next(rdr)
for i in rdr:
    print(i)

    team_name = i[0]

    try:
        # 해당 팀의 TeamList 모델 객체 가져오기
        team_instance = TeamList.objects.get(team=team_name)
    except TeamList.DoesNotExist:
        # Handle the case when the team doesn't exist in TeamList
        # For example, you may want to create the team or handle it differently.
        continue
    # if i[1] == '문경찬':
        # i[26] = 0
            
    # Pitcher 모델에 데이터 저장
    PreRank.objects.create(
        team=team_instance,
        one=i[1],
        two=i[2],
        three=i[3],
        four=i[4],
        five=i[5],
        six=i[6],
        seven=i[7],
        eight = i[8],
        nine = i[9],
        ten = i[10],
    )




# # CSV 파일 읽기
# predictions = pd.read_csv("data/머신머신.csv", index_col=0)

# # 예상된 순위와 확률 출력
# for rank, (team, prob) in enumerate(predictions.iterrows(), start=1):
#     print(f"{rank}위 예상 팀: {team} (확률: {prob.max():.3f})")