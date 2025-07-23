# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the CSV file
# Replace 'sales_data.csv' with your actual CSV file path
df = pd.read_csv('sales_data.csv')

# Step 3: View first few rows
print("First 5 rows of the dataset:")
print(df.head())
# Step 4: Basic info and summary
print("\nBasic Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Step 5: Total sales by product
print("\nTotal Sales by Product:")
product_sales = df.groupby('Product')['Sales'].sum()
print(product_sales)

# Step 6: Total sales by region
print("\nTotal Sales by Region:")
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# Step 7: Total sales by date (if Date column exists)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    daily_sales = df.groupby('Date')['Sales'].sum()
    
    print("\nTotal Sales by Date:")
    print(daily_sales.head())

# Step 8: Plot sales by product
product_sales.plot(kind='bar', title='Total Sales by Product', figsize=(8,5))
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.gri
