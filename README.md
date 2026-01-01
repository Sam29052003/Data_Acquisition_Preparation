# Data_Acquisition_Preparation

# Sub Task 1.1

## Project Overview
                                This project demonstrates the complete data acquisition and preparation workflow using Python in VS Code.  
                                Data is collected from multiple sources, cleaned, analyzed, and visualized to prepare it for further analytics or machine learning tasks.

## Data Sources Used
                              - **Excel File (.xlsx)** – Programmatically created using pandas
                              - **CSV File (.csv)** – Product dataset
                              - **REST API** – JSONPlaceholder Users API

## Tools & Libraries
                                - Python
                                - pandas
                                - requests
                                - openpyxl
                                - matplotlib
                                - VS Code

## Steps Performed

## 1. Data Acquisition
                                 - Created and read Excel data using pandas
                                 - Created and read CSV files
                                 - Extracted data from a REST API

### 2. Data Inspection
                                 - Checked data types and metadata using `.info()`
                                 - Generated summary statistics using `.describe()`

### 3. Data Cleaning
                                 - Handled missing values
                                 - Removed duplicates using a unique identifier
                                 - Renamed columns
                                 - Converted data types

### 4. Exploratory Data Analysis (EDA)
                                 - Bar chart for student marks
                                 - Bar chart for product prices
                                 - Histogram for marks distribution

### 5. Data Saving 
                                  - Saved cleaned datasets for further analysis




# Sub Task 1.2

# Data Cleaning, EDA & Visualization Project

## Project Overview

                           This project focuses on transforming raw, messy datasets into clean, structured, and analysis-ready data using **Python and Pandas**. The cleaned dataset is then explored using                                    **Exploratory Data Analysis (EDA)** and visualized using **Matplotlib**.

## Data Cleaning & Transformation

                                  The following data quality issues were identified and resolved:

                                            * Missing values (imputation)
                                            * Duplicate records removal
                                            * Inconsistent data types correction
                                            * Standardization of text formats
                                            * Irregular and invalid date formats
                                            * Removal of erroneous and noisy values

                                   Multiple datasets were combined using **merge** and **concat** operations to produce a unified dataset.

## Exploratory Data Analysis (EDA)

                                  EDA was performed to understand data distribution, patterns, and relationships.

### Key Analyses:

                                 * Customer age distribution
                                 * Order amount distribution
                                 * Relationship between age and spending
                                 * Total spending per customer
                                 * Monthly customer join trends

## Visualizations Used

                                 * Histogram
                                 * Scatter plot
                                 * Bar chart
                                 * Line chart

                                All visualizations were created using **Matplotlib** in VS Code.

##  Tools & Technologies

                                  * Python
                                  * Pandas
                                  * Matplotlib
                                  * VS Code

##  Project Structure


                                   Boost Track:-
                                   1. data_cleaning.py
                                   2. eda_analysis.py
                                   3. cleaned_unified_data.csv 

##  Outcome

                               The final output is a **cleaned, unified dataset** ready for further analysis and machine learning tasks, along with meaningful insights derived through EDA and visualization.




# Sub Task 1.3 – Initial Exploratory Data Analysis (EDA)

## Objective
                                 The objective of this task is to understand the basic structure, quality, and statistical characteristics of the cleaned dataset before performing full-scale EDA.

## Dataset Used
                                **cleaned_unified_data.csv**

                                The dataset contains customer-related information such as:
                                - Customer ID
                                - Name
                                - City
                                - Age
                                - Purchase Amount
 

## Tools & Technologies
                                - Python 3.14
                                - Pandas
                                - Matplotlib
                                - VS Code


## Steps Performed

### 1. Data Loading
                                - Loaded cleaned dataset using Pandas
                                - Verified dataset structure and size

### 2. Structural Analysis
                                - Inspected column names and data types
                                - Previewed data using head() and tail()

### 3. Data Quality Checks
                               - Missing values detection
                               - Duplicate record detection

### 4. Statistical Analysis
                              - Summary statistics using describe()
                              - Skewness detection
                              - Outlier identification using IQR method

### 5. Initial Visualizations
                              - Histogram for numerical distribution
                              - Boxplot for outliers
                              - Bar chart for categorical distribution
                              - Scatter plot for feature relationships
                              - Correlation matrix for numerical features
## Key Insights
                             - Dataset is clean and well-structured
                             - No missing values or duplicate records
                             - Purchase amount shows mild variability
                             - Certain correlations observed between age and purchase behavior
 
## Outcome
                               The dataset is now fully understood and ready for advanced EDA and machine learning tasks.



## Sub Task 1.4

# Retail Sales Forecasting – Exploratory Data Analysis (EDA)

## Project Overview

                            This project simulates a real-world data preparation and exploratory data analysis workflow for retail sales forecasting.
                            The objective is to analyze a cleaned and integrated retail dataset to understand its structure, quality, patterns, and trends before building forecasting models.

                            This task follows industry-standard practices used by Data Analysts and Data Scientists at the initial stage of a forecasting project.


## Dataset Used

                            File:`cleaned_retail_data.csv`

                           The dataset is created by integrating:

                          * `sales.csv`
                          * `stores.csv`
                          * `products.csv`

### Key Columns

                          * `date` – Sales transaction date
                          * `store_id`, `store_name`, `city` – Store information
                          * `product_id`, `product_name`, `category` – Product details
                          * `quantity` – Units sold
                          * `sales_amount` – Total sales value
                          * `year`, `month`, `week`, `weekday` – Derived time features


## Tools & Technologies

                            **Python 3.14**
                            **Pandas** – Data analysis
                            **Matplotlib** – Data visualization
                            **VS Code** – Development environment


## EDA Steps Performed

### 1. Data Loading & Inspection

                           * Loaded the cleaned dataset using Pandas
                           * Checked shape, column names, and data types
                           * Verified dataset structure and schema

### 2. Data Quality Checks

                           * Checked for missing values
                           * Identified duplicate records
                           * Confirmed data consistency after cleaning

### 3. Statistical Analysis

                          * Generated summary statistics for numerical columns
                          * Analyzed sales distribution and spread
                          * Evaluated skewness and potential outliers

### 4. Exploratory Visualizations

                          * Histogram for sales amount distribution
                          * Boxplot for outlier detection
                          * Bar charts for:

                                          * Store-wise sales
                                          * Product-wise sales

                         * Line plot for daily sales trends
                         * Weekday-wise average sales analysis

### 5. Correlation Analysis

                         * Computed correlation matrix for numerical features
                         * Identified relationships useful for forecasting

## Key Insights

                           * The dataset is clean and well-structured
                           * No missing values or duplicate records detected
                           * Sales show variation across stores and products
                           * Temporal patterns exist across dates and weekdays
                           * The dataset is suitable for time-series forecasting

## Outcome

                          The exploratory data analysis provided a strong understanding of:

                            * Sales behavior
                            * Store and product performance
                            * Temporal trends and seasonality

                            The dataset is now **ready for advanced EDA and forecasting models** such as ARIMA or machine learning approaches.

## Next Steps

                           * Time-series decomposition
                           * Feature engineering for forecasting
                           * Sales prediction models
                           * Model evaluation and business insights





# Task1_Data_Extraction_Cleaning

# Retail Sales Forecasting – Task 1: Data Extraction & Cleaning

## Project Overview
                              This project demonstrates the **end-to-end data preparation workflow** for retail sales forecasting.  
                              The goal is to extract, clean, and integrate multiple datasets to create a unified dataset ready for exploratory data analysis and forecasting.

## Dataset
                              The project uses three CSV files:
                              1. `sales.csv` – transactional sales data
                              2. `stores.csv` – store metadata
                              3. `products.csv` – product metadata

                              All CSV files are located in the `data/` folder.

## Steps Performed

### 1. Data Extraction
                             - Loaded `sales.csv`, `stores.csv`, and `products.csv` using Pandas.

### 2. Data Cleaning
                              - Removed duplicates
                              - Handled missing values
                              - Corrected data types
                              - Standardized text columns (store names, categories)
                              - Fixed date formats

### 3. Data Integration
                             - Merged sales, stores, and products into a single dataset
                             - Ensured referential integrity

### 4. Feature Engineering
                             - Created date-based features: `year`, `month`, `weekday`
                             - Computed basic aggregates: average sales per store and product

### 5. Exploratory Analysis
                            - Summary statistics
                            - Distribution plots of sales
                            - Bar charts for average sales per store/product
                            - Correlation matrix for numeric columns

### 6. Export
                             - Exported final cleaned dataset as `cleaned_retail_data.csv`



## Task-1_Data_Preparation

                              > Task1_Data_Extraction_Cleaning.ipynb
                              > cleaned_retail_data.csv
     
            
             
                                     Data folders
                                     1. sales.csv
                                     2. stores.csv
                                     3. products.csv
