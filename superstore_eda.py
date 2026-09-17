import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Fix dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

# Quick look
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nNull Values:\n", df.isnull().sum())
print("\nBasic Stats:\n", df[['Sales','Profit','Discount','Quantity']].describe())

#Feature Engineering

# New calculated columns
df['Profit Margin']   = df['Profit'] / df['Sales'] * 100
df['Days to Ship']    = (df['Ship Date'] - df['Order Date']).dt.days
df['Is Loss']         = df['Profit'] < 0
df['Profit per Unit'] = df['Profit'] / df['Quantity']
df['Order Month']     = df['Order Date'].dt.to_period('M')
df['Discount Band']   = pd.cut(df['Discount'],
    bins=[-0.01, 0, 0.2, 0.4, 0.6, 1.0],
    labels=['No Discount', '1-20%', '21-40%', '41-60%', '60%+'])

print("New columns added ✅")
print(df[['Profit Margin','Days to Ship','Is Loss','Discount Band']].head())

#Buisness Insights Charts
#Chart 1- Sales and Profit by Region
region = df.groupby('Region')[['Sales','Profit']].sum().sort_values('Profit', ascending=False)
region.plot(kind='bar', figsize=(8,5), color=['#2E75B6','#70AD47'])
plt.title('Sales & Profit by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region'); plt.ylabel('Amount ($)')
plt.xticks(rotation=0); plt.tight_layout(); plt.show()

#Chart 2- Profit by Sub-Category
sub = df.groupby('Sub-Category')['Profit'].sum().sort_values()
colors = ['#FF4444' if x < 0 else '#2E75B6' for x in sub]
sub.plot(kind='barh', figsize=(10,7), color=colors)
plt.title('Profit by Sub-Category', fontsize=14, fontweight='bold')
plt.axvline(0, color='black', linewidth=0.8)
plt.tight_layout(); plt.show()

#Chart 3- Discount vs Profit(The Key Chart)
disc = df.groupby('Discount Band')['Profit'].mean().reset_index()
colors = ['#FF4444' if x < 0 else '#70AD47' for x in disc['Profit']]
plt.figure(figsize=(8,5))
plt.bar(disc['Discount Band'], disc['Profit'], color=colors)
plt.title('Avg Profit by Discount Band', fontsize=14, fontweight='bold')
plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel('Discount Band'); plt.ylabel('Avg Profit ($)')
plt.tight_layout(); plt.show()

#Chart 4- Monthly Sales Trend
monthly = df.groupby('Order Month')['Sales'].sum()
monthly.index = monthly.index.astype(str)
plt.figure(figsize=(14,5))
plt.plot(monthly.index, monthly.values, color='#2E75B6', linewidth=2, marker='o', markersize=4)
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Sales ($)'); plt.tight_layout(); plt.show()

#Chart 5- Sales by Segment(Pie)
seg = df.groupby('Segment')['Sales'].sum()
colors = ['#2E75B6','#70AD47','#ED7D31']
plt.figure(figsize=(7,7))
plt.pie(seg, labels=seg.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Sales by Segment', fontsize=14, fontweight='bold')
plt.tight_layout(); plt.show()

#Chart 6- Top 10 Products by Profit
top10 = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
top10.index = [name[:35]+'...' if len(name)>35 else name for name in top10.index]
top10.plot(kind='barh', figsize=(10,6), color='#1F3864')
plt.title('Top 10 Products by Profit', fontsize=14, fontweight='bold')
plt.xlabel('Total Profit ($)'); plt.tight_layout(); plt.show()