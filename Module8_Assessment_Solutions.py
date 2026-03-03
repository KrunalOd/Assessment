
# ===============================================
# Module 8: NumPy, Pandas, Matplotlib Libraries
# Assessment Solutions
# ===============================================

# ===============================
# Assessment 1 - Bank Data
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Read CSV file
url_bank = "https://raw.githubusercontent.com/TopsCode/Data_Analysis_2024/main/ALL_CSV/banklist.csv"
banks = pd.read_csv(url_bank)

# 2) Show head
print("Head of DataFrame:")
print(banks.head())

# 3) Column names
print("\nColumn Names:")
print(banks.columns)

# 4) How many states
print("\nNumber of States:")
print(banks['ST'].nunique())

# 5) List of states
print("\nList of States:")
print(banks['ST'].unique())

# 6) Top 5 states with most failed banks
print("\nTop 5 States with Most Failed Banks:")
print(banks['ST'].value_counts().head())

# 7) Top 5 acquiring institutions
print("\nTop 5 Acquiring Institutions:")
print(banks['Acquiring Institution'].value_counts().head())

# 8) State Bank of Texas acquisitions
sbt = banks[banks['Acquiring Institution'] == 'State Bank of Texas']
print("\nTotal Acquired by State Bank of Texas:", len(sbt))
print("How many were in Texas:", len(sbt[sbt['ST'] == 'TX']))

# 9) Most common city in California for failure
ca_banks = banks[banks['ST'] == 'CA']
print("\nMost common city in California for failure:")
print(ca_banks['City'].value_counts().head(1))


# ===============================
# Assessment 2 - Automobile Sales
# ===============================

url_auto = "https://raw.githubusercontent.com/TopsCode/Data_Analysis_2024/main/ALL_CSV/historical_automobile_sales.csv"
df = pd.read_csv(url_auto)

# Q1: Line chart for yearly sales
yearly_sales = df.groupby('Year')['Automobile_Sales'].sum()

plt.figure()
yearly_sales.plot()
plt.title("Yearly Automobile Sales")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.show()

# Q2: Sales trend by vehicle type
plt.figure()
vehicle_trend = df.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].sum().unstack()
vehicle_trend.plot()
plt.title("Sales Trend by Vehicle Type")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

# Q3: Seaborn comparison during recession vs non-recession
recession_data = df[df['Recession'] == 1]
non_recession_data = df[df['Recession'] == 0]

plt.figure()
sns.lineplot(data=recession_data, x='Year', y='Automobile_Sales', hue='Vehicle_Type')
plt.title("Sales Trend During Recession")
plt.show()

plt.figure()
sns.lineplot(data=non_recession_data, x='Year', y='Automobile_Sales', hue='Vehicle_Type')
plt.title("Sales Trend During Non-Recession")
plt.show()

# Q4: Bar chart comparing recession vs non-recession
avg_sales = df.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()

plt.figure()
sns.barplot(x='Vehicle_Type', y='Automobile_Sales', hue='Recession', data=avg_sales)
plt.title("Average Sales During Recession vs Non-Recession")
plt.xticks(rotation=45)
plt.show()

print("\nAssessment Completed Successfully!")
