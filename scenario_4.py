import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Setup complete")

df = pd.read_csv(r"C:\Users\hamph\Downloads\marketing_campaign (1).csv", sep="\t")

print(df.head())
print(df.info())

# Missing values
print(df.isnull().sum())

# Handle missing Income
df["Income"] = df["Income"].fillna(df["Income"].mean())

# Create Age
df["Age"] = 2024 - df["Year_Birth"]

# Age Distribution
plt.figure()
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Income Distribution
plt.figure()
plt.boxplot(df["Income"])
plt.title("Income Distribution")
plt.show()

# Total Spending
df["Total_Spending"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)

# Income vs Spending
plt.figure()
plt.scatter(df["Income"], df["Total_Spending"])
plt.title("Income vs Spending")
plt.xlabel("Income")
plt.ylabel("Total Spending")
plt.show()

# Correlation Heatmap
numeric_df = df.select_dtypes(include=np.number)
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()