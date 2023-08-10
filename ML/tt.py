import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the data
df = pd.read_csv('ml.csv')

# Separate features (X) and target (y)
X = df.drop(columns=['kbo_ranking'])
y = df['kbo_ranking']

# One-hot encode categorical data
X_encoded = pd.get_dummies(X)

# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# RandomForestRegressor model
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

# GradientBoostingRegressor model
gb_model = GradientBoostingRegressor(random_state=42)
gb_model.fit(X_train, y_train)

# Model evaluation
y_pred_rf = rf_model.predict(X_test)
y_pred_gb = gb_model.predict(X_test)

mse_rf = mean_squared_error(y_test, y_pred_rf)
mse_gb = mean_squared_error(y_test, y_pred_gb)

print(f"RandomForestRegressor MSE: {mse_rf}")
print(f"GradientBoostingRegressor MSE: {mse_gb}")

# Get the data for 2023 teams from ml.csv
teams_2023 = df[df['year'] == 23]

# Remove the 'team' and 'year' columns
X_2023_data = teams_2023.drop(columns=['team', 'year'])

# One-hot encode the 2023 data
X_2023_encoded = pd.get_dummies(X_2023_data)

# Ensure that the column order matches the original training data
X_2023_scaled = scaler.transform(X_2023_encoded.reindex(columns=X_encoded.columns, fill_value=0))

# RandomForestRegressor prediction for 2023
y_pred_2023_rf = rf_model.predict(X_2023_scaled)

# GradientBoostingRegressor prediction for 2023
y_pred_2023_gb = gb_model.predict(X_2023_scaled)

# Print the predicted rankings for 2023
team_ranking_rf = pd.DataFrame({'Team': teams_2023['team'], 'Predicted_Rank_RF': y_pred_2023_rf})
team_ranking_rf_sorted = team_ranking_rf.sort_values(by='Predicted_Rank_RF')
print("RandomForestRegressor predicted rankings for 2023:")
print(team_ranking_rf_sorted)

team_ranking_gb = pd.DataFrame({'Team': teams_2023['team'], 'Predicted_Rank_GB': y_pred_2023_gb})
team_ranking_gb_sorted = team_ranking_gb.sort_values(by='Predicted_Rank_GB')
print("GradientBoostingRegressor predicted rankings for 2023:")
print(team_ranking_gb_sorted)
