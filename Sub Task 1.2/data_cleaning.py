import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 3, 4],
    "name": ["Amit", "riya", "Rahul ", "Rahul ", None],
    "age": [22, None, 25, 25, 200],
    "join_date": ["2024-01-10", "10/02/2024", "2024.03.15", "2024.03.15", "invalid"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 3, 5],
    "amount": [500, -100, 700, 650]
})

print(customers.info())
print(customers.isnull().sum())

print(orders.info())

customers["name"].fillna("Unknown", inplace=True)
customers["age"].fillna(customers["age"].mean(), inplace=True)

customers.drop_duplicates(subset="customer_id", inplace=True)

customers["name"] = customers["name"].str.strip().str.title()

customers["age"] = customers["age"].astype(int)

customers["join_date"] = pd.to_datetime(
    customers["join_date"],
    errors="coerce"
)

customers = customers[customers["age"] < 100]

orders = orders[orders["amount"] > 0]

print(customers.describe())
print(orders.describe())

final_data = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="inner"
)

extra_orders = pd.DataFrame({
    "order_id": [105],
    "customer_id": [1],
    "amount": [900]
})

orders_all = pd.concat([orders, extra_orders], ignore_index=True)

print(final_data.info())
print(final_data.head())

final_data.to_csv("cleaned_unified_data.csv", index=False)
print("Cleaned unified dataset saved successfully!")

