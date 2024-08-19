import pandas as pd

file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
filtered_customers_df = customers_df[columns_needed]

# Menampilkan beberapa baris pertama dari dataset yang difilter
print(filtered_customers_df.head())

# Menyimpan dataset yang difilter ke file CSV baru
filtered_customers_df.to_csv('filtered_customers_dataset.csv', index=False)
