import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset/amazon_ecommerce_1M.csv")

# Dataset shape
print("Dataset Shape:", df.shape)

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Column-wise Information

print("\nCOLUMN INFORMATION")

for col in df.columns:

    print("\nColumn Name:", col)
    print("Data Type:", df[col].dtype)
    print("Unique Values:", df[col].nunique())
    print("Missing Values:", df[col].isnull().sum())
    
# Numerical Columns

numerical_columns = df.select_dtypes(
    include=np.number
).columns

print("\nNumerical Columns:")
print(numerical_columns)

print("\nNumerical Summary:")

print(df[numerical_columns].describe())

# Categorical Columns

categorical_columns = df.select_dtypes(
    include='object'
).columns

print("\nCategorical Columns:")

for col in categorical_columns:

    print("\n", col)

    print(df[col].value_counts().head(10))
    
# Convert Date Column

df['purchase_date'] = pd.to_datetime(
    df['purchase_date'],
    errors='coerce'
)

print("\nDate Analysis")

print("Minimum Date:", df['purchase_date'].min())

print("Maximum Date:", df['purchase_date'].max())

print("Invalid Dates:", df['purchase_date'].isnull().sum())

# Business Rule Validation

print("\nBUSINESS VALIDATION")

# Price validation
print("Invalid Price:",
      (df['price'] <= 0).sum())

# Discount validation
print("Invalid Discount:",
      ((df['discount'] < 0) |
       (df['discount'] > 100)).sum())

# Final Price validation
print("Invalid Final Price:",
      (df['final_price'] < 0).sum())

# Rating validation
print("Invalid Rating:",
      (~df['rating'].between(1, 5)).sum())

# Seller Rating validation
print("Invalid Seller Rating:",
      (~df['seller_rating'].between(1, 5)).sum())

# Stock validation
print("Invalid Stock:",
      (df['stock'] < 0).sum())

# Shipping Time validation
print("Invalid Shipping Time:",
      (df['shipping_time_days'] < 0).sum())

# Verify Discount Calculation

expected_price = (
    df['price'] * (1 - df['discount'] / 100)
)

price_difference = (
    df['final_price'] - expected_price
).abs()

print(
    "Discount Calculation Mismatch:",
    (price_difference > 0.02).sum()
)

# Business Insights

print("\nTOTAL CUSTOMERS:")
print(df['user_id'].nunique())

print("\nTOTAL PRODUCTS:")
print(df['product_id'].nunique())

print("\nTOTAL SELLERS:")
print(df['seller_id'].nunique())

print("\nTOP 10 CATEGORIES:")
print(df['category'].value_counts().head(10))

print("\nPAYMENT METHOD DISTRIBUTION:")
print(df['payment_method'].value_counts())

print("\nRETURNED PRODUCTS:")
print(df['is_returned'].value_counts())

print("\nDELIVERY STATUS:")
print(df['delivery_status'].value_counts())


# INVESTIGATE DISCOUNT MISMATCH

expected_price = df['price'] * (1 - df['discount'] / 100)

price_difference = df['final_price'] - expected_price

print("\nDISCOUNT MISMATCH INVESTIGATION")

print("Exact Matches:", (price_difference.abs() <= 0.02).sum())

print("Mismatches:", (price_difference.abs() > 0.02).sum())

print("\nPrice Difference Statistics:")
print(price_difference.describe())

print("\nSample Mismatched Records:")

mismatch_data = df.loc[
    price_difference.abs() > 0.02,
    ['price', 'discount', 'final_price']
].copy()

mismatch_data['expected_price'] = expected_price[
    price_difference.abs() > 0.02
]

mismatch_data['price_difference'] = price_difference[
    price_difference.abs() > 0.02
]

print(mismatch_data.head(10))

# ABSOLUTE PRICE DIFFERENCE ANALYSIS

absolute_difference = price_difference.abs()

print("\nABSOLUTE PRICE DIFFERENCE ANALYSIS")

print("Difference <= 0.05:",
      (absolute_difference <= 0.05).sum())

print("Difference <= 0.10:",
      (absolute_difference <= 0.10).sum())

print("Difference <= 0.50:",
      (absolute_difference <= 0.50).sum())

print("Difference <= 1.00:",
      (absolute_difference <= 1.00).sum())

print("Difference > 1.00:",
      (absolute_difference > 1.00).sum())

print("\nLargest Differences:")

largest_mismatches = df.loc[
    absolute_difference.nlargest(10).index,
    ['price', 'discount', 'final_price']
].copy()

largest_mismatches['expected_price'] = expected_price.loc[
    largest_mismatches.index
]

largest_mismatches['difference'] = price_difference.loc[
    largest_mismatches.index
]

print(largest_mismatches)

# ROUNDING INVESTIGATION

rounded_expected_price = expected_price.round(2)

rounding_difference = (
    df['final_price'] - rounded_expected_price
).abs()

print("\nROUNDING INVESTIGATION")

print(
    "Exact matches after rounding:",
    (rounding_difference == 0).sum()
)

print(
    "Differences within 0.01:",
    (rounding_difference <= 0.01).sum()
)

print(
    "Differences greater than 0.01:",
    (rounding_difference > 0.01).sum()
)

print("\nRounding Difference Statistics:")
print(rounding_difference.describe())

# PRICE DIFFERENCE PATTERN ANALYSIS

print("\nPRICE DIFFERENCE PATTERN ANALYSIS")

# Relative difference in percentage
relative_difference_pct = (
    price_difference / expected_price
) * 100

print("\nRelative Difference Statistics:")
print(relative_difference_pct.describe())

print("\nAbsolute Relative Difference Statistics:")
print(relative_difference_pct.abs().describe())


# Positive and negative differences
print("\nDifference Direction:")

print(
    "Positive Differences:",
    (price_difference > 0).sum()
)

print(
    "Negative Differences:",
    (price_difference < 0).sum()
)

print(
    "Zero Differences:",
    (price_difference == 0).sum()
)


# Price range analysis
df['price_band'] = pd.cut(
    df['price'],
    bins=[0, 1000, 5000, 10000, 20000, 40000, 60000, 80000]
)

df['absolute_difference'] = price_difference.abs()

price_band_analysis = df.groupby(
    'price_band',
    observed=False
)['absolute_difference'].agg(
    ['count', 'mean', 'max']
)

print("\nPrice Band Analysis:")
print(price_band_analysis)