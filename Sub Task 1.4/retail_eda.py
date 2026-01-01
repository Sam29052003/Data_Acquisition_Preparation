import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned retail dataset
df = pd.read_csv("cleaned_retail_data.csv")

print("Dataset loaded successfully")
print("Shape:", df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns)

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- DATA INFO ---")
print(df.info())

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- LAST 5 ROWS ---")
print(df.tail())

print("\n--- SUMMARY STATISTICS ---")
print(df.describe())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

df["sales_amount"].hist()
plt.title("Sales Amount Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()

plt.boxplot(df["sales_amount"])
plt.title("Sales Amount Outliers")
plt.ylabel("Sales Amount")
plt.show()

df.groupby("date")["sales_amount"].sum().plot()
plt.title("Daily Total Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

df.groupby("store_name")["sales_amount"].sum().plot(kind="bar")
plt.title("Total Sales by Store")
plt.xlabel("Store")
plt.ylabel("Total Sales")
plt.show()

df.groupby("product_name")["sales_amount"].sum().plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

df.groupby("weekday")["sales_amount"].mean().plot(kind="bar")
plt.title("Average Sales by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Average Sales")
plt.show()

print("\n--- CORRELATION MATRIX ---")
print(df.select_dtypes(include="number").corr())

