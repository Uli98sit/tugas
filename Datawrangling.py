# Importing essential libraries
import pandas as pd
import numpy as np

# Step 1: Load the dataset
# Assuming the dataset is in a CSV file named 'customers_dataset.csv'
# Replace 'path_to_your_dataset' with the actual path where the dataset is stored
dataset = pd.read_csv('path_to_your_dataset/customers_dataset.csv')

# Step 2: Display the first few rows of the dataset
print("First few rows of the dataset:")
print(dataset.head())

# Step 3: Check for missing values
print("\nChecking for missing values:")
missing_values = dataset.isnull().sum()
print(missing_values[missing_values > 0])

# Step 4: Handle missing values
# Option 1: Drop rows with missing values (if appropriate)
dataset_cleaned = dataset.dropna(subset=['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state'])

# Step 5: Handle duplicate rows
print("\nChecking for duplicate rows based on 'customer_unique_id':")
duplicate_rows = dataset_cleaned.duplicated(subset=['customer_unique_id']).sum()
print(f"Number of duplicate rows based on 'customer_unique_id': {duplicate_rows}")

# If there are duplicate customer_unique_id, remove them
dataset_cleaned = dataset_cleaned.drop_duplicates(subset=['customer_unique_id'])

# Step 6: Standardize the 'customer_city' and 'customer_state' columns
# Example: Convert city and state names to title case
dataset_cleaned['customer_city'] = dataset_cleaned['customer_city'].str.title()
dataset_cleaned['customer_state'] = dataset_cleaned['customer_state'].str.upper()

# Step 7: Convert 'customer_zip_code_prefix' to string to ensure consistent formatting
dataset_cleaned['customer_zip_code_prefix'] = dataset_cleaned['customer_zip_code_prefix'].astype(str)

# Step 8: Check the final dataset
print("\nFinal dataset overview:")
print(dataset_cleaned.info())
print("\nFirst few rows of the cleaned dataset:")
print(dataset_cleaned.head())

# Save the cleaned dataset to a new CSV file (optional)
# dataset_cleaned.to_csv('path_to_save_cleaned_dataset/cleaned_customers_dataset.csv', index=False)