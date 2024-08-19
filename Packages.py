# Importing essential libraries
import pandas as pd          # For data manipulation and analysis
import numpy as np           # For numerical operations

# Loading the dataset
# Assuming the dataset is in a CSV file named 'customers_dataset.csv'
# Replace 'path_to_your_dataset' with the actual path where the dataset is stored
dataset = pd.read_csv('path_to_your_dataset/customers_dataset.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(dataset.head())

# Check for missing values
print("\nChecking for missing values:")
missing_values = dataset.isnull().sum()
print(missing_values[missing_values > 0])

# Handle missing values
# Option 1: Drop rows with missing values in key columns
dataset_cleaned = dataset.dropna(subset=['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state'])

# Handle duplicate rows
print("\nChecking for duplicate rows based on 'customer_unique_id':")
duplicate_rows = dataset_cleaned.duplicated(subset=['customer_unique_id']).sum()
print(f"Number of duplicate rows based on 'customer_unique_id': {duplicate_rows}")

# Remove duplicate rows if any
dataset_cleaned = dataset_cleaned.drop_duplicates(subset=['customer_unique_id'])

# Standardize the 'customer_city' and 'customer_state' columns
dataset_cleaned['customer_city'] = dataset_cleaned['customer_city'].str.title()
dataset_cleaned['customer_state'] = dataset_cleaned['customer_state'].str.upper()

# Convert 'customer_zip_code_prefix' to string
dataset_cleaned['customer_zip_code_prefix'] = dataset_cleaned['customer_zip_code_prefix'].astype(str)

# Final check of the cleaned dataset
print("\nFinal dataset overview:")
print(dataset_cleaned.info())
print("\nFirst few rows of the cleaned dataset:")
print(dataset_cleaned.head())

# Save the cleaned dataset to a new CSV file (optional)
# dataset_cleaned.to_csv('path_to_save_cleaned_dataset/cleaned_customers_dataset.csv', index=False)