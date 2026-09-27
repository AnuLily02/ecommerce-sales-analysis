import pandas as pd
import matplotlib.pyplot as plt


# Load datasets
details = pd.read_csv("C:/Users/Anupama/OneDrive/Desktop/ecommerce-sales-analysis/Data/Details.csv")
orders = pd.read_csv("C:/Users/Anupama/OneDrive/Desktop/ecommerce-sales-analysis/Data/Orders.csv")

#details and orders Dataset
print("Details Dataset")
print("=" * 50)
print(details.head())

print("\nOrders Dataset")
print("=" * 50)
print(orders.head())

#details and orders information 
print("\nDetails Information")
print("=" * 50)
print(details.info())

print("\nOrders Information")
print("=" * 50)
print(orders.info())

#to list 
print("\nDetails Columns:")
print(details.columns.tolist())

print("\nOrders Columns:")
print(orders.columns.tolist())

#checking for missing values
print("\nMissing Values - Details")
print(details.isnull().sum())

print("\nMissing Values - Orders")
print(orders.isnull().sum())

# checking for any duplicate values
print("\nDuplicate rows in Details:", details.duplicated().sum())
print("Duplicate rows in Orders:", orders.duplicated().sum())

# merging two dataset ....here both dataset as order id in common 
df = pd.merge(
    details,
    orders,
    on="Order ID",
    how="left"
)
# printing the combined dataset 
print("\nCombined Dataset")
print("=" * 50)
print(df.head())

#checking the merged dataset
print("\nCombined Dataset Shape:")
print(df.shape)

print("\nCombined Dataset Information:")
print(df.info())

# checking for missing values in merged dataset 
print("\nMissing Values After Merge:")
print(df.isnull().sum())


#converting the date into actual date format 
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

print("\nDate Range:")
print(df["Order Date"].min())
print(df["Order Date"].max())


#Basic Sales Analysis
total_sales = df["Amount"].sum()

print("\nTotal Sales:")
print(total_sales)

total_profit = df["Profit"].sum()

print("\nTotal Profit:")
print(total_profit)

#Total quantity
total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")
print(total_quantity)

#average orders value
average_order = df["Amount"].mean()

print("\nAverage Order Amount:")
print(average_order)

#higest-value order
highest_order = df.loc[df["Amount"].idxmax()]

print("\nHighest Value Order:")
print(highest_order)

#Category Analysis
category_sales = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Category:")
print(category_sales)

#Sub-Category Analysis
subcategory_sales = (
    df.groupby("Sub-Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Sub-Category:")
print(subcategory_sales)

#Payment Method Analysis
payment_analysis = df["PaymentMode"].value_counts()

print("\nOrders by Payment Method:")
print(payment_analysis)

#State Analysis
state_sales = (
    df.groupby("State")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by State:")
print(state_sales)


#City Analysis (Top 10 only)
city_sales = (
    df.groupby("City")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by City:")
print(city_sales.head(10))

#Customer Analysis
customer_sales = (
    df.groupby("CustomerName")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Customers:")
print(customer_sales.head(10))


#Monthly Sales 
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Amount"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)


#Monthly Profit
monthly_profit = (
    df.groupby("Month")["Profit"]
    .sum()
)

print("\nMonthly Profit:")
print(monthly_profit) 


#Category Sales Chart
plt.figure(figsize=(10, 6))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "C:/Users/Anupama/OneDrive/Desktop/ecommerce-sales-analysis/outputs/charts/sales_by_category.png"
)

plt.show()