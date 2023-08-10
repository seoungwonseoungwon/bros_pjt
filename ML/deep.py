import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

# KBO_TRAIN.csv 파일 로드
train_data = pd.read_csv("KBO_TRAIN.csv")

# 데이터 전처리
X_train = train_data.drop(['SEASON', 'TEAM', 'GRADE'], axis=1)
y_train = train_data['GRADE']

# 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 머신러닝 모델 학습
model = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# 테스트 데이터 로드
test_data = pd.read_csv("KBO_TEST.csv")

# 데이터 전처리
X_test = test_data.drop(['SEASON', 'TEAM', 'GRADE'], axis=1)
y_test = test_data['GRADE']

# 스케일링
X_test_scaled = scaler.transform(X_test)

# 테스트 데이터로 예측
y_pred = model.predict(X_test_scaled)

# 예측 결과 출력
print("테스트 데이터 예측 결과:")
print(y_pred)
