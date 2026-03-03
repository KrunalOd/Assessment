
# ======================================================
# DA Assessment - Python Libraries (Complete Solution)
# Libraries Used: Pandas, NumPy, Matplotlib, Seaborn
# ======================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ======================================================
# ================= FINANCIAL ANALYSIS =================
# ======================================================

finance_url = "https://raw.githubusercontent.com/Priya-tops/Tops-Assessment-Data/main/Data%20Analytics/finance_economics_dataset.csv"
df = pd.read_csv(finance_url)

print("Shape of Dataset:", df.shape)
print("\nColumns & Data Types:\n", df.dtypes)
print("\nUnique Stock Indices:", df['Stock_Index'].nunique())
print("\nDate Range:", df['Date'].min(), "to", df['Date'].max())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

print("\nGDP Growth Summary:\n", df['GDP_Growth (%)'].describe())
print("\nInflation Summary:\n", df['Inflation Rate (%)'].describe())
print("\nAverage Unemployment Rate:", df['Unemployment Rate (%)'].mean())
print("\nHighest Gold Price:", df['Gold Price'].max())
print("\nHighest Oil Price Date:", df.loc[df['Crude Oil Price'].idxmax(), 'Date'])
print("\nAverage Corporate Profit:", df['Corporate Profits'].mean())

print("\nCorrelation (Inflation vs Interest Rate):",
      df['Inflation Rate (%)'].corr(df['Interest Rate (%)']))

print("\nHighest Std Deviation Column:\n", df.std(numeric_only=True).sort_values(ascending=False).head(1))

# Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=False)
plt.title("Correlation Heatmap - Financial Data")
plt.show()


# ======================================================
# ================= RETAIL SALES ANALYSIS =============
# ======================================================

retail_url = "https://raw.githubusercontent.com/Priya-tops/Tops-Assessment-Data/main/Data%20Analytics/Retail%20Data.csv"
retail = pd.read_csv(retail_url)

print("\nRetail Dataset Shape:", retail.shape)
print("\nRetail Data Types:\n", retail.dtypes)
print("\nDuplicate Records:", retail.duplicated().sum())
print("\nMissing Values:\n", retail.isnull().sum())

# Convert Dates
retail['Order Date'] = pd.to_datetime(retail['Order Date'], errors='coerce')
retail['Ship Date'] = pd.to_datetime(retail['Ship Date'], errors='coerce')

# Shipping Duration
retail['Shipping_Days'] = (retail['Ship Date'] - retail['Order Date']).dt.days

print("\nUnique Customer Types:", retail['Customer Type'].unique())
print("\nUnique Order Priorities:", retail['Order Priority'].unique())
print("\nMost Common Shipping Mode:\n", retail['Ship Mode'].value_counts().head())
print("\nTop Cities by Orders:\n", retail['City'].value_counts().head())

print("\nOrder Quantity Range:", retail['Quantity'].min(), "to", retail['Quantity'].max())
print("\nAverage Shipping Cost by Mode:\n",
      retail.groupby('Ship Mode')['Shipping Cost'].mean())

print("\nTop 5 Products by Quantity:\n",
      retail.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head())

print("\nAccount Manager with Most Revenue:\n",
      retail.groupby('Account Manager')['Total'].sum().sort_values(ascending=False).head(1))

print("\nMost Profitable Product:\n",
      retail.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(1))

print("\nTotal Revenue:", retail['Total'].sum())
print("\nAverage Discount %:", retail['Discount'].mean())
print("\nAverage Order Spend:", retail['Total'].mean())

# Revenue by Customer Type
plt.figure()
retail.groupby('Customer Type')['Total'].sum().plot(kind='bar')
plt.title("Revenue by Customer Type")
plt.show()

print("\nAssessment Completed Successfully!")
