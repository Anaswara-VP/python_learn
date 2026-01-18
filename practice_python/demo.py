# 📊 SALES DATA VISUALIZATION AND ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_dataset.csv")

# Display first few rows
print("Preview of Dataset:")
print(df.head(), "\n")

# Basic summary
print("Dataset Info:")
print(df.info(), "\n")

print("Descriptive Statistics:")
print(df.describe(), "\n")

# -----------------------------
# 1️⃣ TOTAL SALES BY REGION
# -----------------------------
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

plt.figure(figsize=(6,4))
sns.barplot(x="Region", y="Sales", data=region_sales, palette="Blues_d")
plt.title("Total Sales by Region (Jan–Jun)")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# -----------------------------
# 2️⃣ TOTAL PROFIT BY REGION
# -----------------------------
region_profit = df.groupby("Region")["Profit"].sum().reset_index()

plt.figure(figsize=(6,4))
sns.barplot(x="Region", y="Profit", data=region_profit, palette="Greens_d")
plt.title("Total Profit by Region (Jan–Jun)")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# -----------------------------
# 3️⃣ MONTHLY SALES TREND
# -----------------------------
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

plt.figure(figsize=(8,4))
sns.lineplot(x="Month", y="Sales", data=monthly_sales, marker="o", color="royalblue")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# -----------------------------
# 4️⃣ SALES BY PRODUCT CATEGORY
# -----------------------------
product_sales = df.groupby("Product")["Sales"].sum().reset_index()

plt.figure(figsize=(6,4))
sns.barplot(x="Product", y="Sales", data=product_sales, palette="Oranges_d")
plt.title("Total Sales by Product Category")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# -----------------------------
# 5️⃣ PRODUCT SALES DISTRIBUTION (PIE CHART)
# -----------------------------
plt.figure(figsize=(5,5))
plt.pie(product_sales["Sales"], labels=product_sales["Product"], autopct='%1.1f%%', startangle=140)
plt.title("Product-wise Sales Distribution")
plt.show()
