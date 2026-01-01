import pandas as pd

# Sample unified clean dataset
data = {
    "customer_id": [101, 102, 103, 104, 105],
    "customer_name": ["Amit", "Riya", "Rahul", "Sneha", "Karan"],
    "city": ["Pune", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "age": [23, 25, 22, 24, 26],
    "purchase_amount": [2500, 3200, 1800, 2900, 4100]
}

df = pd.DataFrame(data)

# Save clean dataset
df.to_csv("cleaned_unified_data.csv", index=False)

print("cleaned_unified_data.csv created successfully")
print(df)

