-- 01_database_setup.sql

-- 1. Create Database

CREATE DATABASE IF NOT EXISTS ecommerce_customer_intelligence;


-- 2. Select Database

USE ecommerce_customer_intelligence;


-- 3. Create Ecommerce Data Table

CREATE TABLE IF NOT EXISTS ecommerce_data (

    user_id VARCHAR(50),
    product_id VARCHAR(50),

    category VARCHAR(100),
    subcategory VARCHAR(100),
    brand VARCHAR(100),

    price DECIMAL(12,2),
    discount DECIMAL(5,2),
    final_price DECIMAL(12,2),

    rating DECIMAL(3,2),
    review_count INT,
    stock INT,

    seller_id VARCHAR(50),
    seller_rating DECIMAL(3,2),

    purchase_date DATE,
    shipping_time_days INT,

    location VARCHAR(100),
    device VARCHAR(50),
    payment_method VARCHAR(50),

    is_returned TINYINT(1),
    delivery_status VARCHAR(50)

);


-- 4. Verify Database

SHOW DATABASES;


-- 5. Verify Table

SHOW TABLES;


-- 6. Check Table Structure

DESCRIBE ecommerce_data;


