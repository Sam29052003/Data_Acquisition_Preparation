import pandas as pd


# SALES DATA
sales_data = {
    "sale_id": [1, 2, 3, 4, 5],
    "store_id": [101, 101, 102, 103, 102],
    "product_id": [1001, 1002, 1001, 1003, 1002],
    "date": ["2024-01-05", "2024-01-06", "2024-01-07", "2024-01-08", "2024-01-09"],
    "quantity": [2, 1, 3, 2, 4],
    "sales_amount": [500, 300, 750, 600, 1200]
}

pd.DataFrame(sales_data).to_csv("sales.csv", index=False)


# STORES DATA
stores_data = {
    "store_id": [101, 102, 103],
    "store_name": ["Central Mall", "City Store", "Mega Mart"],
    "city": ["Pune", "Mumbai", "Delhi"]
}

pd.DataFrame(stores_data).to_csv("stores.csv", index=False)


# PRODUCTS DATA

products_data = {
    "product_id": [1001, 1002, 1003],
    "product_name": ["Laptop", "Mobile", "Headphones"],
    "category": ["Electronics", "Electronics", "Accessories"]
}

pd.DataFrame(products_data).to_csv("products.csv", index=False)

print("All CSV files created successfully")
