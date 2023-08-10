import pandas as pd

# 2023년의 KBO 순위 데이터를 딕셔너리로 생성합니다.
data_2023 = {
    'year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'team': ['LG', 'SSG', '두산', 'NC', '롯데', 'KT', 'KIA', '한화', '키움', '삼성'],
    'kbo_ranking': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# 2022년의 KBO 순위 데이터를 딕셔너리로 생성합니다.
data_2022 = {
    'year': [2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022],
    'team': ['SSG', 'LG', 'KT', '키움', 'KIA', 'NC', '삼성', '롯데', '두산', '한화'],
    'kbo_ranking': [1, 2, 3, 3, 5, 6, 7, 8, 9, 10]
}

# 2021년의 KBO 순위 데이터를 딕셔너리로 생성합니다.
data_2021 = {
    'year': [2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021],
    'team': ['KT', '삼성', 'LG', '두산', '키움', 'SSG', 'NC', '롯데', 'KIA', '한화'],
    'kbo_ranking': [1, 1, 3, 4, 5, 6, 7, 8, 6, 3]
}

# 2020년의 KBO 순위 데이터를 딕셔너리로 생성합니다.
data_2020 = {
    'year': [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020],
    'team': ['NC', 'KT', '두산', 'LG', '키움', 'KIA', '롯데', '삼성', 'SK', '한화'],
    'kbo_ranking': [1, 2, 3, 3, 5, 6, 7, 8, 9, 10]
}

# DataFrame을 생성합니다.
data_2023_df = pd.DataFrame(data_2023)
data_2022_df = pd.DataFrame(data_2022)
data_2021_df = pd.DataFrame(data_2021)
data_2020_df = pd.DataFrame(data_2020)

# DataFrame을 하나로 합칩니다.
kbo_ranking_data_all = pd.concat([data_2023_df, data_2022_df, data_2021_df, data_2020_df], ignore_index=True)

# 합쳐진 DataFrame을 CSV 파일로 저장합니다.
kbo_ranking_data_all.to_csv('kbo_ranking_data_all.csv', index=False)

# 생성한 파일을 확인합니다.
print("CSV 파일 'kbo_ranking_data_all.csv'이(가) 생성되었습니다.")
