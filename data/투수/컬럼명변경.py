import pandas as pd

# Assuming you have already read the CSV file into a DataFrame called 'df_pitcher'
# Replace 'df_pitcher' with the actual variable name of your DataFrame

# Define the new column names
new_columns = {
    '순': 'id',
    '이름': 'name',
    '팀': 'team',
    'WAR': 'war',
    '출장': 'games_played',
    '완투': 'complete_games',
    '완봉': 'shutouts',
    '선발': 'games_started',
    '승': 'wins',
    '패': 'losses',
    '세': 'saves',
    '홀드': 'holds',
    '이닝': 'innings_pitched',
    '실점': 'runs_allowed',
    '자책': 'earned_runs',
    '타자': 'batters_faced',
    '안타': 'hits_allowed',
    '2타': 'doubles_allowed',
    '3타': 'triples_allowed',
    '홈런': 'home_runs_allowed',
    '볼넷': 'walks_allowed',
    '고4': 'hit_by_pitch',
    '사구': 'intentional_walks',
    '삼진': 'strikeouts',
    '보크': 'balks',
    '폭투': 'wild_pitches',
    'ERA': 'era',
    'FIP': 'fip',
    'WHIP': 'whip',
    'ERA+': 'era_plus',
    'FIP+': 'fip_plus',
    'WAR.1': 'war_another_source',
    'WPA': 'wpa'
}

# Rename the columns in the DataFrame
aa.rename(columns=new_columns, inplace=True)

# Now the DataFrame 'df_pitcher' will have the updated column names