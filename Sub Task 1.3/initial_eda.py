import pandas as pd

# Load dataset
df = pd.read_csv("cleaned_unified_data.csv")

print("Dataset loaded successfully")

print("\n--- BASIC STRUCTURE ---")
print("Shape (Rows, Columns):", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- LAST 5 ROWS ---")
print(df.tail())

print("\n--- SUMMARY STATISTICS (NUMERICAL) ---")
print(df.describe())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Number of duplicate rows:", df.duplicated().sum())

print("\n--- CATEGORICAL VALUE COUNTS ---")

for col in df.select_dtypes(include="object").columns:
    print(f"\nColumn: {col}")
    print(df[col].value_counts())

print("\n--- NUMERICAL COLUMN SKEWNESS ---")

for col in df.select_dtypes(include="number").columns:
    print(f"{col}: skew = {df[col].skew():.2f}")


print("\n--- OUTLIER CHECK (IQR METHOD) ---")

for col in df.select_dtypes(include="number").columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
    print(f"{col}: Outliers = {outliers.shape[0]}")


print("\n--- CORRELATION MATRIX ---")
correlation = df.select_dtypes(include="number").corr()
print(correlation)


