# E-COMMERCE CUSTOMER INTELLIGENCE & ANALYTICS

## 1. Project Overview

The E-Commerce Customer Intelligence & Analytics project focuses on analyzing e-commerce purchase records to understand customer behavior, product performance, seller performance, and return patterns.

The project uses Python for data cleaning, preprocessing, feature engineering, and exploratory data analysis. MySQL is used to perform basic and advanced SQL analysis, while Power BI is used to create an interactive dashboard for visualizing key business metrics and analytical findings.

The dataset contains 1,000,000 purchase records with information about customers, products, categories, brands, sellers, pricing, ratings, payment methods, delivery status, and returns.

Customer segmentation is also performed using RFM (Recency, Frequency, Monetary) analysis to identify different customer groups based on their purchasing behavior.

The main objective is to transform raw e-commerce data into meaningful insights that can support data-driven business decisions.

## 2. Problem Statement

E-commerce businesses generate large amounts of data through customer purchases, product interactions, seller activities, payment methods, and delivery operations.

Analyzing this information manually can be difficult and time-consuming.

This project addresses the need to organize, process, and analyze e-commerce data to identify customer purchasing patterns, understand product and seller performance, evaluate return behavior, and present useful insights through an interactive dashboard.

## 3. Project Objectives

- Analyze customer purchasing behavior.
- Identify top-performing product categories and brands.
- Evaluate seller performance using purchase records, observed spending, and ratings.
- Analyze customer retention and repeat purchasing patterns.
- Perform customer segmentation using RFM analysis.
- Understand return patterns and delivery performance.
- Perform SQL-based business analysis.
- Build an interactive Power BI dashboard.
- Generate meaningful insights from e-commerce data.

## 4. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Data cleaning and analysis |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| MySQL | Database management and SQL analysis |
| Power BI | Interactive dashboard development |
| DAX | Calculated measures and analytical calculations |
| Visual Studio Code | Python development and project management |
| MySQL Workbench | SQL execution and database management |

## 5. Dataset Description

The project uses an e-commerce sample dataset containing 1,000,000 purchase records and 20 original columns.

The dataset includes customer, product, seller, pricing, rating, payment, shipping, delivery, and return information.

### 5.1 Dataset Statistics

| Description | Value |
|---|---:|
| Total Records | 1,000,000 |
| Original Columns | 20 |
| Feature-Engineered Columns | 29 |
| Unique Customers | 603,815 |
| Unique Products | 89,999 |
| Unique Sellers | 9,000 |
| Date Range | 31 March 2024 – 31 March 2026 |
| Returned Records | 115,990 |

### 5.2 Original Column Description

| Column Name | Description |
|---|---|
| user_id | Customer identifier |
| product_id | Product identifier |
| category | Product category |
| subcategory | Product subcategory |
| brand | Product brand |
| price | Original product price |
| discount | Discount percentage |
| final_price | Recorded final product price |
| rating | Product rating |
| review_count | Number of product reviews |
| stock | Available stock |
| seller_id | Seller identifier |
| seller_rating | Seller rating |
| purchase_date | Purchase record date |
| shipping_time_days | Shipping time in days |
| location | Customer location |
| device | Device used for purchase |
| payment_method | Payment method |
| is_returned | Return indicator |
| delivery_status | Delivery status |

## 6. Data Cleaning Using Python

Data cleaning was performed using Python and Pandas.

The original dataset was loaded and inspected to understand its structure, data types, and quality.

The following operations were performed:

- Loaded the original CSV dataset.
- Checked dataset dimensions and column information.
- Inspected missing values.
- Checked duplicate records.
- Converted the purchase_date column into datetime format.
- Validated numeric columns and their values.
- Investigated pricing-related inconsistencies.
- Prepared the cleaned dataset for further analysis.

### Data Cleaning Results

- Total records: 1,000,000.
- Missing values: None found.
- Duplicate rows: None found.
- Invalid numeric values: None identified through the validation checks.

The cleaned dataset was saved as:

`cleaned_ecommerce.csv`

## 7. Feature Engineering

Feature engineering was performed to create additional analytical variables from the original dataset.

The project added 9 derived columns, increasing the dataset from 20 to 29 columns.

These additional features helped prepare the data for customer analysis, time-based analysis, and dashboard development.

The feature-engineered dataset was saved as:

`feature_engineered_ecommerce.csv`

The resulting dataset was used for exploratory data analysis, customer analysis, and Power BI dashboard creation.

## 8. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the distribution and patterns present in the dataset.

The analysis covered:

- Product category distribution.
- Brand-level purchase record distribution.
- Monthly purchase record trends.
- Payment method distribution.
- Return patterns across product categories.
- Product rating analysis.

Visualizations were created using Matplotlib to understand these patterns.

### EDA Visualizations

The following charts were generated:

1. Category Distribution.
2. Monthly Distribution.
3. Return Rate by Category.

These visualizations helped identify patterns in product categories, purchase activity, and return behavior.

## 9. Customer Analysis and RFM Segmentation

Customer analysis was performed to understand purchasing frequency, observed spending, and customer activity.

RFM analysis was used to segment customers based on three dimensions:

- Recency: Time since the customer's latest recorded purchase.
- Frequency: Number of purchase records associated with the customer.
- Monetary: Sum of recorded final_price values associated with the customer.

RFM scores were calculated using quintile-based scoring, and customers were grouped into five project-specific segments.

### 9.1 Customer Statistics

| Metric | Value |
|---|---:|
| Unique Customers | 603,815 |
| One-Time Customers | 329,745 |
| Repeat Customers | 274,070 |
| One-Time Customer Percentage | 54.61% |
| Repeat Customer Percentage | 45.39% |

### 9.2 RFM Customer Segments

| Customer Segment | Customer Count |
|---|---:|
| Potential | 188,265 |
| Loyal | 168,362 |
| At Risk | 106,114 |
| Champions | 97,400 |
| Hibernating | 43,674 |

### 9.3 RFM Analysis Findings

- Potential customers represent the largest customer segment.
- Loyal customers form another significant group.
- Champions represent customers with strong recorded purchasing activity.
- At Risk and Hibernating segments can be considered for customer engagement analysis.
- The repeat customer percentage is 45.39%, based on customers with more than one purchase record.

The RFM analysis results were saved as:

`customer_rfm_analysis.csv`

## 10. SQL Analysis Using MySQL

MySQL was used to perform structured queries and analyze the e-commerce dataset.

A database named:

`ecommerce_customer_intelligence`

was created.

The main table used for analysis was:

`ecommerce_data`

The MySQL import dataset was prepared using Python to convert the return indicator into a numeric format.

### 10.1 Basic SQL Analysis

The basic SQL analysis included:

- Total record count.
- Unique customer count.
- Product category analysis.
- Brand analysis.
- Payment method distribution.
- Return analysis.
- Monthly purchase record analysis.

### 10.2 Advanced SQL Analysis

Advanced SQL queries were performed using:

- Common Table Expressions (CTEs).
- Window functions and ranking.
- CASE statements.
- Customer spending analysis.
- Seller performance analysis.
- Customer segmentation queries.

These queries helped explore customer, product, and seller-related patterns in a structured database environment.

## 11. Power BI Dashboard Development

Power BI was used to create an interactive five-page dashboard named:

**E-Commerce Customer Intelligence**

The dashboard was designed with a consistent layout, navigation sidebar, KPI cards, and analytical visualizations.

### 11.1 Page 1: Home – Executive Overview

The Home page provides an overview of the dataset through five KPI cards:

- Total Records: 1M
- Unique Customers: 604K
- Average Rating: 3.93
- Unique Products: 90K
- Return Rate: 11.60%

Visualizations:

- Purchase Records by Category.
- Monthly Purchase Trend.
- Return Rate by Category.

### 11.2 Page 2: Sales & Product Analysis

This page focuses on product and payment-related analysis.

Visualizations:

- Top 10 Brands by Purchase Records.
- Purchase Records by Payment Method.
- Top 10 Product Subcategories.
- Average Rating by Category.

### 11.3 Page 3: Customer Intelligence

This page focuses on customer behavior and segmentation.

Visualizations:

- Customer RFM Segmentation.
- Top 10 Customers by Observed Spending.
- One-Time vs Repeat Customers.
- Customer Purchase Frequency Distribution.

### 11.4 Page 4: Seller Performance Analysis

This page evaluates seller performance.

Visualizations:

- Top 10 Sellers by Purchase Records.
- Top 10 Sellers by Observed Spending.
- Top 10 Sellers by Average Rating.

### 11.5 Page 5: Returns & Delivery Analysis

This page focuses on returns and shipping-related patterns.

Visualizations:

- Delivery Status Distribution.
- Return Rate by Payment Method.
- Monthly Return Rate Trend.
- Average Shipping Time by Delivery Status.

## 12. Key Business Insights

Based on the analysis performed, the following observations were identified:

### Customer Insights

- The dataset contains 603,815 unique customers.
- Approximately 54.61% of customers have one purchase record.
- Approximately 45.39% have multiple purchase records.
- Potential is the largest RFM customer segment.

### Product Insights

- Product category and brand-level purchase record distributions were analyzed.
- Product subcategories were ranked to identify the top-performing groups.
- Average product ratings were compared across categories.

### Seller Insights

- Sellers were ranked based on purchase record counts.
- Seller-level observed spending was compared.
- Average seller ratings were used to identify highly rated sellers.

### Returns and Delivery Insights

- The overall return rate is approximately 11.60%.
- A total of 115,990 records are marked as returned.
- Return rates were compared across product categories and payment methods.
- Monthly return rate patterns were visualized.
- Average shipping time was compared across delivery statuses.

## 13. Project Limitations

The following limitations should be considered while interpreting the results:

- The project uses an e-commerce sample dataset and does not represent verified internal business data from a specific company.
- The dataset does not contain an order_id or basket identifier. Therefore, purchase record counts should not be interpreted as verified order counts.
- Frequency represents the number of customer purchase records, not confirmed order frequency.
- Monetary represents observed spending calculated from recorded final_price values and should not be treated as verified company revenue.
- The final_price values do not perfectly match price after applying the discount percentage. The recorded final_price values were preserved for analysis.
- March 2024 and March 2026 are partial years, so annual and monthly comparisons should be interpreted carefully.
- RFM segment names are project-specific classifications based on the scoring approach used.

## 14. Conclusion

The E-Commerce Customer Intelligence & Analytics project demonstrates an end-to-end data analytics workflow using Python, MySQL, and Power BI.

Python was used for data understanding, cleaning, feature engineering, exploratory analysis, and customer segmentation.

MySQL was used to perform structured queries and analyze customer, product, and seller-related information.

Power BI was used to develop a five-page interactive dashboard covering executive metrics, product performance, customer intelligence, seller performance, and returns and delivery analysis.

The project helped develop practical skills in data preprocessing, analytical thinking, SQL querying, customer segmentation, data visualization, and dashboard development.

Overall, this project demonstrates how raw e-commerce sample data can be transformed into structured information and meaningful analytical insights.

---

**Project Name:** E-Commerce Customer Intelligence & Analytics

**Tools Used:** Python, Pandas, NumPy, Matplotlib, MySQL, Power BI, DAX, Visual Studio Code

**Project Type:** End-to-End Data Analytics Project