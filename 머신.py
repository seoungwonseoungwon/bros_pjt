import csv
import pandas as pd

f = open("data/머신머신.csv", "r", encoding='utf-8')
reader = csv.reader(f)

for i in reader:
    print(i)




# # CSV 파일 읽기
# predictions = pd.read_csv("data/머신머신.csv", index_col=0)

# # 예상된 순위와 확률 출력
# for rank, (team, prob) in enumerate(predictions.iterrows(), start=1):
#     print(f"{rank}위 예상 팀: {team} (확률: {prob.max():.3f})")