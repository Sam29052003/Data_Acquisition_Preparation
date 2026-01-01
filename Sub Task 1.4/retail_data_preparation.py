import pandas as pd
import numpy as np

# Load CSV files
sales = pd.read_csv("sales.csv")
stores = pd.read_csv("stores.csv")
products = pd.read_csv("products.csv")

print("Datasets loaded successfully")

print("\nSales Shape:", sales.shape)
print("Stores Shape:", stores.shape)
print("Products Shape:", products.shape)

print("\n--- SALES INFO ---")
print(sales.info())

print("\n--- STORES INFO ---")
print(stores.info())

print("\n--- PRODUCTS INFO ---")
print(products.info())

sales.drop_duplicates(inplace=True)
stores.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)

print("Duplicates removed")

# Sales
sales["sales_amount"].fillna(sales["sales_amount"].median(), inplace=True)
sales["quantity"].fillna(0, inplace=True)

# Stores
stores["store_name"].fillna("Unknown Store", inplace=True)
stores["city"].fillna("Unknown City", inplace=True)

# Products
products["product_name"].fillna("Unknown Product", inplace=True)
products["category"].fillna("Unknown Category", inplace=True)

print("Missing values handled")

# Convert date column
sales["date"] = pd.to_datetime(sales["date"], errors="coerce")

# Numeric conversions
sales["sales_amount"] = sales["sales_amount"].astype(float)
sales["quantity"] = sales["quantity"].astype(int)

print("Data types corrected")

stores["store_name"] = stores["store_name"].str.strip().str.title()
stores["city"] = stores["city"].str.strip().str.title()

products["product_name"] = products["product_name"].str.strip().str.title()
products["category"] = products["category"].str.strip().str.upper()

print("Text standardized")

# Keep only valid foreign keys
sales = sales[
    sales["store_id"].isin(stores["store_id"]) &
    sales["product_id"].isin(products["product_id"])
]

print("Referential integrity ensured")

# Merge sales with stores
merged_df = pd.merge(
    sales,
    stores,
    on="store_id",
    how="left"
)

# Merge with products
merged_df = pd.merge(
    merged_df,
    products,
    on="product_id",
    how="left"
)

print("Datasets merged successfully")
print("Final Shape:", merged_df.shape)

merged_df["year"] = merged_df["date"].dt.year
merged_df["month"] = merged_df["date"].dt.month
merged_df["week"] = merged_df["date"].dt.isocalendar().week
merged_df["weekday"] = merged_df["date"].dt.day_name()

print("Date features created")

# Average weekly sales per store
avg_store_sales = (
    merged_df
    .groupby(["store_id", "week"])["sales_amount"]
    .mean()
    .reset_index()
)

# Average sales per product
avg_product_sales = (
    merged_df
    .groupby("product_id")["sales_amount"]
    .mean()
    .reset_index()
)

print("Basic summaries computed")

merged_df.to_csv("cleaned_retail_data.csv", index=False)

print("cleaned_retail_data.csv saved successfully")

