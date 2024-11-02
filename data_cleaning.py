import pandas as pd

# Load the dataset
data = pd.read_csv('train.csv')  # Ensure your dataset is in the same directory

# Step 1: Drop the "Cabin" column due to a high percentage of missing values
data_cleaned = data.drop(columns=["Cabin"])

# Step 2: Drop rows with missing values in "Embarked"
data_cleaned = data_cleaned.dropna(subset=["Embarked"])

# Step 3: Impute missing values in "Age" with the median age
age_median = data_cleaned["Age"].median()
data_cleaned["Age"].fillna(age_median, inplace=True)

# Step 4: Define function to remove outliers using IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]

# Remove outliers for "Age" and "Fare"
data_cleaned = remove_outliers(data_cleaned, "Age")
data_cleaned = remove_outliers(data_cleaned, "Fare")

# Save the cleaned dataset
data_cleaned.to_csv('cleaned_data.csv', index=False)
