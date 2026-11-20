import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv(
    "dataset/feature_engineered_ecommerce.csv",
    parse_dates=["purchase_date"]
)

print("Dataset Shape:", df.shape)


# 1. UNIQUE CUSTOMER ANALYSIS

print("\nUNIQUE CUSTOMER ANALYSIS")

total_customers = df['user_id'].nunique()

print("Total Unique Customers:", total_customers)


# 2. CUSTOMER PURCHASE FREQUENCY

print("\nCUSTOMER PURCHASE FREQUENCY")

customer_frequency = df.groupby('user_id').size()

print("\nPurchase Frequency Summary:")
print(customer_frequency.describe())

repeat_customers = (customer_frequency > 1).sum()

one_time_customers = (customer_frequency == 1).sum()

print("\nOne-Time Customers:", one_time_customers)
print("Repeat Customers:", repeat_customers)

print(
    "Repeat Customer Percentage:",
    round((repeat_customers / total_customers) * 100, 2),
    "%"
)


# 3. CUSTOMER REVENUE ANALYSIS

print("\nCUSTOMER REVENUE ANALYSIS")

customer_revenue = df.groupby('user_id').agg(
    total_records=('final_price', 'count'),
    total_spending=('final_price', 'sum'),
    average_spending=('final_price', 'mean')
)

print("\nTop 10 Customers by Spending:")

print(
    customer_revenue.sort_values(
        by='total_spending',
        ascending=False
    ).head(10)
)


# 4. RFM ANALYSIS

print("\nRFM ANALYSIS")

snapshot_date = df['purchase_date'].max() + pd.Timedelta(days=1)

rfm = df.groupby('user_id').agg(
    recency=('purchase_date', lambda x: (snapshot_date - x.max()).days),
    frequency=('purchase_date', 'count'),
    monetary=('final_price', 'sum')
)

print("\nRFM Summary:")
print(rfm.describe())


# 5. RFM SCORING

# Recency: Lower recency is better
rfm['R_score'] = pd.qcut(
    rfm['recency'].rank(method='first'),
    5,
    labels=[5, 4, 3, 2, 1]
).astype(int)


# Frequency: Higher frequency is better
rfm['F_score'] = pd.qcut(
    rfm['frequency'].rank(method='first'),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)


# Monetary: Higher spending is better
rfm['M_score'] = pd.qcut(
    rfm['monetary'].rank(method='first'),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)


# 6. RFM TOTAL SCORE

rfm['RFM_score'] = (
    rfm['R_score']
    + rfm['F_score']
    + rfm['M_score']
)


# 7. CUSTOMER SEGMENTATION

def customer_segment(score):

    if score >= 13:
        return 'Champions'

    elif score >= 10:
        return 'Loyal Customers'

    elif score >= 7:
        return 'Potential Customers'

    elif score >= 5:
        return 'At Risk'

    else:
        return 'Hibernating'


rfm['customer_segment'] = rfm['RFM_score'].apply(
    customer_segment
)


# 8. SEGMENT ANALYSIS

print("\nCUSTOMER SEGMENT DISTRIBUTION")

segment_analysis = rfm['customer_segment'].value_counts()

print(segment_analysis)


print("\nAVERAGE METRICS BY CUSTOMER SEGMENT")

segment_metrics = rfm.groupby('customer_segment').agg(
    customers=('recency', 'count'),
    average_recency=('recency', 'mean'),
    average_frequency=('frequency', 'mean'),
    average_monetary=('monetary', 'mean')
)

print(segment_metrics)


# 9. SAVE CUSTOMER ANALYSIS

rfm.to_csv(
    "reports/customer_rfm_analysis.csv"
)

print("\nCustomer RFM Analysis Saved Successfully!")

print("Total Customers Analysed:", len(rfm))