import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv("dataset/amazon_ecommerce_1M.csv")

print("Original Dataset Shape:", df.shape)


# 1. Convert purchase_date to datetime
df['purchase_date'] = pd.to_datetime(
    df['purchase_date'],
    errors='coerce'
)


# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# 3. Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())


# 4. Check data types
print("\nData Types:")
print(df.dtypes)


# 5. Check invalid numerical values
print("\nInvalid Values:")

print("Invalid Price:", (df['price'] <= 0).sum())

print(
    "Invalid Discount:",
    ((df['discount'] < 0) | (df['discount'] > 100)).sum()
)

print("Invalid Final Price:", (df['final_price'] < 0).sum())

print(
    "Invalid Rating:",
    ((df['rating'] < 0) | (df['rating'] > 5)).sum()
)


# 6. Check return status consistency
print("\nReturn Status Analysis:")

print(
    pd.crosstab(
        df['is_returned'],
        df['delivery_status']
    )
)


# 7. Save cleaned dataset
df.to_csv(
    "dataset/cleaned_ecommerce.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully!")

print("Final Dataset Shape:", df.shape)