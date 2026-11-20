import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Feature Engineered Dataset

df = pd.read_csv(
    "dataset/feature_engineered_ecommerce.csv"
)

print("Dataset Shape:", df.shape)


# 1. Category Analysis

print("\nCATEGORY ANALYSIS")

category_analysis = df.groupby('category').agg(
    total_records=('product_id', 'count'),
    average_price=('price', 'mean'),
    average_final_price=('final_price', 'mean'),
    average_rating=('rating', 'mean')
).sort_values(
    by='total_records',
    ascending=False
)

print(category_analysis)


# 2. Brand Analysis

print("\nBRAND ANALYSIS")

brand_analysis = df.groupby('brand').agg(
    total_records=('product_id', 'count'),
    average_rating=('rating', 'mean'),
    average_price=('final_price', 'mean')
).sort_values(
    by='total_records',
    ascending=False
)

print(brand_analysis)


# 3. Monthly Analysis

print("\nMONTHLY ANALYSIS")

monthly_analysis = df.groupby('purchase_month').agg(
    total_records=('product_id', 'count'),
    average_final_price=('final_price', 'mean')
).sort_index()

print(monthly_analysis)


# 4. Payment Method Analysis

print("\nPAYMENT METHOD ANALYSIS")

payment_analysis = df.groupby('payment_method').agg(
    total_records=('product_id', 'count'),
    average_final_price=('final_price', 'mean')
).sort_values(
    by='total_records',
    ascending=False
)

print(payment_analysis)


# 5. Return Analysis

print("\nRETURN ANALYSIS")

return_analysis = df.groupby('category').agg(
    total_records=('is_returned', 'count'),
    returned_records=('is_returned', 'sum')
)

return_analysis['return_rate'] = (
    return_analysis['returned_records']
    / return_analysis['total_records']
) * 100

print(return_analysis)


# 6. Visualizations

# Category Distribution

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x='category',
    order=df['category'].value_counts().index
)

plt.title("Category Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/category_distribution.png")
plt.show()


# Monthly Distribution

plt.figure(figsize=(10, 5))

sns.barplot(
    data=monthly_analysis.reset_index(),
    x='purchase_month',
    y='total_records'
)

plt.title("Monthly Purchase Distribution")
plt.xlabel("Month")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("reports/monthly_distribution.png")
plt.show()


# Return Rate by Category

plt.figure(figsize=(10, 5))

sns.barplot(
    data=return_analysis.reset_index(),
    x='category',
    y='return_rate'
)

plt.title("Return Rate by Category")
plt.ylabel("Return Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/return_rate_by_category.png")
plt.show()


print("\nEDA Completed Successfully!")