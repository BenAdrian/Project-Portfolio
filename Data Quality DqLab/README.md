# 📊 Data Quality with Python for Beginner
 ----------------------------------------
This script is based on a learning module from DQLab, focusing on understanding and applying data quality concepts using Python.

# The process is divided into two main phases:
 1. Data Profiling
 2. Data Cleansing

# 🔍 1. Data Profiling
This is the initial step where we examine the structure, contents, and overall quality of the dataset before performing further analysis.

## Steps included:
- Data type inspection: Check that each column has the correct data type (e.g., numeric, object, datetime)
- Descriptive Statistics:
     - len(): Total number of rows
     - count(): Number of non-null entries per column
     - isnull().sum(): Number and percentage of missing values
     - min(), max(): Find smallest and largest values in numeric columns
     - quantile(): Understand data spread (Q1, median, Q3)
     - corr(): Examine correlation between numerical columns

## Tools used: pandas


# 🧹 2. Data Cleansing
Once the dataset is profiled, we proceed to clean it to ensure it is reliable and ready for analysis.

## Steps included:
 - Handle missing values (using dropna() or fillna())
 - Deal with outliers (e.g., via IQR or Z-score method)
 - Remove duplicate entries (using drop_duplicates())
 - Fix inconsistent formats (e.g., convert date formats, standardize text cases)

## Tools used: pandas and numpy

# 📁 Note:
 This project is part of my self-learning documentation as I grow my data analysis skills using Python.

