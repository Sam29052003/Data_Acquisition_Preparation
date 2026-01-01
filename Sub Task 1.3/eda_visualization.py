import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_unified_data.csv")

print("Dataset Loaded Successfully")

# 1. Histogram (Numerical Distribution)

df["age"].hist()
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 2. Boxplot (Outlier Detection)

plt.boxplot(df["purchase_amount"])
plt.title("Purchase Amount Outliers")
plt.ylabel("Amount")
plt.show()

# 3. Bar Chart (Categorical Distribution)

df["city"].value_counts().plot(kind="bar")
plt.title("Customers by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

# 4. Scatter Plot (Relationship)

plt.scatter(df["age"], df["purchase_amount"])
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.show()


# 5. Correlation Heatmap (Text Output Safe)

print("\nCorrelation Matrix:")
print(df.select_dtypes(include="number").corr())
