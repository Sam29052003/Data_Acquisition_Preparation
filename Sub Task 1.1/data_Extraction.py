
# DATA ACQUISITION, EDA & VISUALIZATION

import pandas as pd
import requests
import matplotlib.pyplot as plt


# STEP 1: CREATE & READ EXCEL DATA

excel_data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Amit", "Riya", "Rahul", "Sneha", "Karan"],
    "marks": [85, 90, 78, 88, 92]
}

df_excel_create = pd.DataFrame(excel_data)
df_excel_create.to_excel("data.xlsx", index=False, engine="openpyxl")

df_excel = pd.read_excel("data.xlsx", engine="openpyxl")
print("\nExcel Data:")
print(df_excel.head())



# STEP 2: CREATE & READ CSV DATA

csv_data = {
    "product_id": [101, 102, 103, 104],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [55000, 800, 1500, 12000]
}

df_csv_create = pd.DataFrame(csv_data)
df_csv_create.to_csv("data.csv", index=False)

df_csv = pd.read_csv("data.csv")
print("\nCSV Data:")
print(df_csv.head())


# STEP 3: API DATA EXTRACTION

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

df_api = pd.DataFrame(response.json())
print("\nAPI Data:")
print(df_api.head())



# STEP 4: DATA INSPECTION (EDA)

print("\nExcel Info:")
print(df_excel.info())

print("\nCSV Info:")
print(df_csv.info())

print("\nAPI Info:")
print(df_api.info())



# STEP 5: DATA CLEANING

# Handle missing values
df_api.fillna("Not Available", inplace=True)

# Remove duplicates safely
df_api.drop_duplicates(subset="id", inplace=True)

# Rename column
df_api.rename(columns={"username": "user_name"}, inplace=True)

# Type conversion
df_excel["marks"] = df_excel["marks"].astype(int)



# STEP 6: EDA STATISTICS

print("\nExcel Descriptive Statistics:")
print(df_excel.describe())

print("\nCSV Descriptive Statistics:")
print(df_csv.describe())



# STEP 7: VISUALIZATION (EDA PLOTS)

# Plot 1: Marks distribution
plt.figure()
plt.bar(df_excel["name"], df_excel["marks"])
plt.title("Student Marks Distribution")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

# Plot 2: Product prices
plt.figure()
plt.bar(df_csv["product_name"], df_csv["price"])
plt.title("Product Price Comparison")
plt.xlabel("Product Name")
plt.ylabel("Price")
plt.show()

# Plot 3: Marks histogram
plt.figure()
plt.hist(df_excel["marks"])
plt.title("Marks Frequency Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()



# STEP 8: SAVE CLEANED DATA

df_excel.to_csv("cleaned_excel_data.csv", index=False)
df_csv.to_csv("cleaned_csv_data.csv", index=False)
df_api.to_csv("cleaned_api_data.csv", index=False)

print("\nAll cleaned datasets saved successfully!")
print("EDA & Visualization completed successfully!")
