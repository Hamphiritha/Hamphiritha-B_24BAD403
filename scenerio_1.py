import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


folder_path = r"C:\Users\hamph\Downloads\data.csv"
print(os.listdir(folder_path))  # make sure data.csv exists


df = pd.read_csv(r"C:\Users\hamph\Downloads\data.csv\data.csv", encoding='latin1')


print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())


df['Sales'] = df['Quantity'] * df['UnitPrice']


product_sales = (
    df.groupby('Description')['Sales']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(product_sales)


plt.figure(figsize=(10,6))
product_sales.plot(kind='bar')
plt.xlabel("Product Description")
plt.ylabel("Total Sales")
plt.title("Top 10 Products by Sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,6))
product_sales.plot(kind='line', marker='o')
plt.xlabel("Product Description")
plt.ylabel("Total Sales")
plt.title("Sales Trend of Top 10 Products")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

