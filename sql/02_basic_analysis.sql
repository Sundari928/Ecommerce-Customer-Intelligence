-- 02_basic_analysis.sql
USE ecommerce_customer_intelligence;

-- 1. Overall Business Overview

SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT user_id) AS unique_customers,
    COUNT(DISTINCT product_id) AS unique_products,
    COUNT(DISTINCT seller_id) AS unique_sellers,
    ROUND(AVG(rating), 2) AS average_rating,
    ROUND(AVG(final_price), 2) AS average_final_price,
    SUM(is_returned) AS total_returns,
    ROUND(AVG(is_returned) * 100, 2) AS return_percentage
FROM ecommerce_data;

-- 2. Category Performance Analysis

SELECT
    category,
    COUNT(*) AS total_records,
    COUNT(DISTINCT user_id) AS unique_customers,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(AVG(final_price), 2) AS average_final_price,
    ROUND(AVG(rating), 2) AS average_rating,
    SUM(is_returned) AS total_returns,
    ROUND(AVG(is_returned) * 100, 2) AS return_percentage

FROM ecommerce_data

GROUP BY category

ORDER BY total_records DESC;

-- 3. Brand Performance Analysis

SELECT
    brand,
    COUNT(*) AS total_records,
    COUNT(DISTINCT user_id) AS unique_customers,
    ROUND(AVG(final_price), 2) AS average_final_price,
    ROUND(AVG(rating), 2) AS average_rating,
    SUM(is_returned) AS total_returns,
    ROUND(AVG(is_returned) * 100, 2) AS return_percentage

FROM ecommerce_data

GROUP BY brand

ORDER BY total_records DESC

LIMIT 10;

-- 4. Payment Method Analysis

SELECT
    payment_method,
    COUNT(*) AS total_records,
    COUNT(DISTINCT user_id) AS unique_customers,
    ROUND(AVG(final_price), 2) AS average_final_price,
    SUM(is_returned) AS total_returns,
    ROUND(AVG(is_returned) * 100, 2) AS return_percentage

FROM ecommerce_data

GROUP BY payment_method

ORDER BY total_records DESC;

-- 5. Return Rate Analysis

SELECT
    category,
    COUNT(*) AS total_records,
    SUM(is_returned) AS returned_records,

    COUNT(*) - SUM(is_returned) AS non_returned_records,

    ROUND(
        AVG(is_returned) * 100, 2
    ) AS return_percentage,

    ROUND(AVG(rating), 2) AS average_rating

FROM ecommerce_data

GROUP BY category

ORDER BY return_percentage DESC;

-- 6. Monthly Performance Analysis

SELECT
    YEAR(purchase_date) AS purchase_year,
    MONTH(purchase_date) AS purchase_month,
    MONTHNAME(purchase_date) AS month_name,

    COUNT(*) AS total_records,

    ROUND(AVG(final_price), 2) AS average_final_price,

    ROUND(SUM(final_price), 2) AS total_observed_spending,

    SUM(is_returned) AS returned_records,

    ROUND(AVG(is_returned) * 100, 2) AS return_percentage

FROM ecommerce_data

GROUP BY
    YEAR(purchase_date),
    MONTH(purchase_date),
    MONTHNAME(purchase_date)

ORDER BY
    purchase_year,
    purchase_month;