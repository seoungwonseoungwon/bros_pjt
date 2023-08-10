import pandas as pd

# Load the dataset
df = pd.read_csv('ml.csv')

# Split the data into training (year 23) and testing (other years) sets
train_data = df[df['year'] == 23]
test_data = df[df['year'] != 23]

# Save the training and testing datasets to separate CSV files
train_data.to_csv('KBO_TRAIN.csv', index=False)
test_data.to_csv('KBO_TEST.csv', index=False)
