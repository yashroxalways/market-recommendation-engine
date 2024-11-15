import os
import pandas as pd

# Assuming the dataset contains a CSV file. Adjust filename as necessary.
dataset_path = 'C:/Users/user/market recommendation engine'

# Check if the file exists
if os.path.exists(dataset_path):
    # Load dataset
    df = pd.read_csv(dataset_path)
    print("Dataset loaded successfully.")
    print("Dataset preview:")
    print(df.head())  # Display first few rows of the dataset
else:
    print(f"Dataset not found at {dataset_path}")
