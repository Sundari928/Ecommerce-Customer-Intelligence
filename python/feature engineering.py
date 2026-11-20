import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv(
    "dataset/cleaned_ecommerce.csv",
    parse_dates=["purchase_date"]
)

print("Dataset Shape:", df.shape)


# 1. Date Features

df['purchase_year'] = df['purchase_date'].dt.year

df['purchase_month'] = df['purchase_date'].dt.month

df['purchase_month_name'] = df['purchase_date'].dt.month_name()

df['purchase_quarter'] = df['purchase_date'].dt.quarter

df['purchase_day'] = df['purchase_date'].dt.day

df['purchase_weekday'] = df['purchase_date'].dt.day_name()


# 2. Discount Amount

df['discount_amount'] = df['price'] - df['final_price']


# 3. Discount Percentage Based on Observed Prices

df['actual_discount_percentage'] = (
    df['discount_amount'] / df['price']
) * 100


# 4. Shipping Category

df['shipping_category'] = np.where(
    df['shipping_time_days'] <= 2,
    'Fast',
    np.where(
        df['shipping_time_days'] <= 4,
        'Standard',
        'Slow'
    )
)


# 5. Display New Columns

new_columns = [
    'purchase_year',
    'purchase_month',
    'purchase_month_name',
    'purchase_quarter',
    'purchase_day',
    'purchase_weekday',
    'discount_amount',
    'actual_discount_percentage',
    'shipping_category'
]

print("\nNew Feature Preview:")
print(df[new_columns].head())


# 6. Summary

print("\nShipping Category Distribution:")
print(df['shipping_category'].value_counts())

print("\nYear Distribution:")
print(df['purchase_year'].value_counts().sort_index())

print("\nMonthly Distribution:")
print(df['purchase_month_name'].value_counts())


# 7. Save Feature Engineered Dataset

df.to_csv(
    "dataset/feature_engineered_ecommerce.csv",
    index=False
)

print("\nFeature Engineered Dataset Saved Successfully!")

print("Final Shape:", df.shape)