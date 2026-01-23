from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

print("Setup complete")

# Correct file path
file_path = (r"C:\Users\hamph\Downloads\diabetes (1).csv")

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found!")

# Load dataset with correct encoding
df = pd.read_csv(file_path, encoding="latin1")

# Inspect dataset
print(df.head())
print(df.tail())
df.info()
print(df.describe())

# Check missing values
missing_values = df.isnull().sum()
print(missing_values)

# Columns where 0 means missing
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

# Count zero values
zero_values = (df[cols] == 0).sum()
print("\nZero values (treated as missing):")
print(zero_values)

# Replace zero values with NaN
df[cols] = df[cols].replace(0, np.nan)

# Histogram
plt.figure()
plt.hist(df["Glucose"].dropna(), bins=20)
plt.title("Distribution of Glucose Levels")
plt.xlabel("Glucose Level")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure()
plt.boxplot(df["Age"].dropna())
plt.title("Age Distribution of Patients")
plt.ylabel("Age")
plt.show()

# Group analysis
health_patterns = df.groupby("Outcome").mean(numeric_only=True)
print("\nMean Health Metrics by Outcome:")
print(health_patterns)
