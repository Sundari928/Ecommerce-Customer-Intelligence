-- 03_advanced_analysis.sql
USE ecommerce_customer_intelligence;

-- 1. Top 10 Customers by Observed Spending

SELECT
    user_id,
    COUNT(*) AS total_records,
    ROUND(SUM(final_price), 2) AS total_spending,
    ROUND(AVG(final_price), 2) AS average_spending,
    MAX(purchase_date) AS last_purchase_date
FROM ecommerce_data
GROUP BY user_id
ORDER BY total_spending DESC
LIMIT 10;

-- 2. Rank Top 20 Customers by Observed Spending

SELECT
    user_id,
    total_records,
    total_spending,
    RANK() OVER (ORDER BY total_spending DESC) AS customer_rank,
    DENSE_RANK() OVER (ORDER BY total_spending DESC) AS dense_customer_rank
FROM (
    SELECT
        user_id,
        COUNT(*) AS total_records,
        SUM(final_price) AS total_spending
    FROM ecommerce_data
    GROUP BY user_id
) AS customer_summary
ORDER BY total_spending DESC
LIMIT 20;

-- 3. High Value Customer Analysis using CTE

WITH customer_spending AS (
    SELECT
        user_id,
        COUNT(*) AS total_records,
        SUM(final_price) AS total_spending,
        AVG(final_price) AS average_spending
    FROM ecommerce_data
    GROUP BY user_id
)

SELECT
    user_id,
    total_records,
    ROUND(total_spending, 2) AS total_spending,
    ROUND(average_spending, 2) AS average_spending
FROM customer_spending
WHERE total_spending > (
    SELECT AVG(total_spending)
    FROM customer_spending
)
ORDER BY total_spending DESC
LIMIT 20;

-- 4. Customer Segmentation using CASE WHEN

WITH customer_summary AS (
    SELECT
        user_id,
        COUNT(*) AS total_records,
        SUM(final_price) AS total_spending
    FROM ecommerce_data
    GROUP BY user_id
)

SELECT
    user_id,
    total_records,
    ROUND(total_spending, 2) AS total_spending,

    CASE
        WHEN total_records = 1 THEN 'One-Time Customer'
        WHEN total_records BETWEEN 2 AND 3 THEN 'Repeat Customer'
        ELSE 'Frequent Customer'
    END AS customer_segment

FROM customer_summary
ORDER BY total_records DESC
LIMIT 50;

-- 5. Seller Performance Analysis

SELECT
    seller_id,
    COUNT(*) AS total_records,
    COUNT(DISTINCT user_id) AS unique_customers,
    ROUND(AVG(final_price), 2) AS average_selling_price,
    ROUND(AVG(seller_rating), 2) AS average_seller_rating,
    SUM(is_returned) AS total_returns,
    ROUND(AVG(is_returned) * 100, 2) AS return_percentage

FROM ecommerce_data

GROUP BY seller_id

HAVING COUNT(*) >= 50

ORDER BY average_seller_rating DESC

LIMIT 20;