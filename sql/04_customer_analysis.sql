USE ecommerce_customer_intelligence;


-- 1. One-Time vs Repeat Customer Analysis

SELECT
    customer_type,
    COUNT(*) AS customer_count
FROM (
    SELECT
        user_id,
        CASE
            WHEN COUNT(*) = 1 THEN 'One-Time Customer'
            ELSE 'Repeat Customer'
        END AS customer_type
    FROM ecommerce_data
    GROUP BY user_id
) AS customer_summary
GROUP BY customer_type;


-- 2. Customer Purchase Frequency Distribution

SELECT
    purchase_frequency,
    COUNT(*) AS customer_count
FROM (
    SELECT
        user_id,
        COUNT(*) AS purchase_frequency
    FROM ecommerce_data
    GROUP BY user_id
) AS frequency_summary
GROUP BY purchase_frequency
ORDER BY purchase_frequency;


-- 3. Customer Recency Analysis

SELECT
    user_id,
    MAX(purchase_date) AS last_purchase_date,
    DATEDIFF(
        DATE_ADD(
            (SELECT MAX(purchase_date) FROM ecommerce_data),
            INTERVAL 1 DAY
        ),
        MAX(purchase_date)
    ) AS recency_days
FROM ecommerce_data
GROUP BY user_id
ORDER BY recency_days DESC;


-- 4. Customer Frequency and Monetary Analysis

SELECT
    user_id,
    COUNT(*) AS frequency,
    ROUND(SUM(final_price), 2) AS monetary
FROM ecommerce_data
GROUP BY user_id
ORDER BY monetary DESC;


-- 5. Customer RFM Base Analysis

SELECT
    user_id,

    DATEDIFF(
        DATE_ADD(
            (SELECT MAX(purchase_date) FROM ecommerce_data),
            INTERVAL 1 DAY
        ),
        MAX(purchase_date)
    ) AS recency,

    COUNT(*) AS frequency,

    ROUND(SUM(final_price), 2) AS monetary

FROM ecommerce_data
GROUP BY user_id
ORDER BY monetary DESC;