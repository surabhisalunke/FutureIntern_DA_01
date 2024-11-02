# FutureIntern_DA_01
# TASK 1: Data Cleaning Task

This script cleans the Titanic dataset by handling missing values and removing outliers.

## Steps:
1. Removes columns with excessive missing values (e.g., Cabin).
2. Imputes missing values in the Age column with the median.
3. Drops rows with missing Embarked values.
4. Identifies and removes outliers in Age and Fare columns using the IQR method.

## Usage:
1. Run `data_cleaning.py` in the repository directory.
2. The cleaned dataset will be saved as `cleaned_data.csv`.
