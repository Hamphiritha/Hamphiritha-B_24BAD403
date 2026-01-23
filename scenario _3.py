import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Setup complete")

df = pd.read_csv(r"C:\Users\hamph\Downloads\Housing (1).csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:
    df[col] = df[col].map({"yes": 1, "no": 0})

plt.figure()
plt.scatter(df["area"], df["price"])
plt.title("Area vs House Price")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.show()

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap of Housing Features")
plt.show()

print("\nKey Observations:")
print("- Area has strong correlation with price")
print("- Number of bathrooms and stories impact price")
print("- Furnishing and parking also influence house value")