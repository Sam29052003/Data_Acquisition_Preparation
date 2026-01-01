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
