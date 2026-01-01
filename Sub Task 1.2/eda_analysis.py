import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_unified_data.csv")

print(df.head())
print(df.info())

# Shape of data
print("Rows & Columns:", df.shape)

# Statistical summary
print(df.describe())

# Check missing values
print(df.isnull().sum())

plt.figure()
plt.hist(df["age"], bins=5)
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df["amount"], bins=5)
plt.title("Order Amount Distribution")
plt.xlabel("Order Amount")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df["age"], df["amount"])
plt.title("Age vs Order Amount")
plt.xlabel("Age")
plt.ylabel("Order Amount")
plt.show()

customer_spending = df.groupby("name")["amount"].sum()

plt.figure()
customer_spending.plot(kind="bar")
plt.title("Total Spending per Customer")
plt.xlabel("Customer Name")
plt.ylabel("Total Amount")
plt.show()

df["join_date"] = pd.to_datetime(df["join_date"])

join_trend = df.groupby(df["join_date"].dt.month)["customer_id"].count()

plt.figure()
join_trend.plot(kind="line")
plt.title("Customer Join Trend by Month")
plt.xlabel("Month")
plt.ylabel("Number of Customers")
plt.show()
