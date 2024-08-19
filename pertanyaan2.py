import pandas as pd

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkanimport pandas as pd

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_zip_code_prefix']
filtered_customers_df = customers_df[columns_needed]

# Menghitung jumlah kode pos yang unik
unique_zip_codes = filtered_customers_df['customer_zip_code_prefix'].nunique()

print(f"\nJumlah Kode Pos Unik di Dataset: {unique_zip_codes}")
columns_needed = ['customer_zip_code_prefix']
filtered_customers_df = customers_df[columns_needed]

# Menghitung jumlah kode pos yang unik
unique_zip_codes = filtered_customers_df['customer_zip_code_prefix'].nunique()

print(f"\nJumlah Kode Pos Unik di Dataset: {unique_zip_codes}")