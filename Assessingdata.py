import pandas as pd

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
filtered_customers_df = customers_df[columns_needed]

# 1. Menampilkan informasi umum tentang dataset
print("Informasi Umum Dataset:")
print(filtered_customers_df.info())

# 2. Menampilkan statistik deskriptif
print("\nStatistik Deskriptif:")
print(filtered_customers_df.describe())

# 3. Menampilkan jumlah data yang hilang
print("\nJumlah Data yang Hilang di Setiap Kolom:")
print(filtered_customers_df.isnull().sum())

# 4. Menampilkan distribusi nilai unik di setiap kolom
print("\nDistribusi Nilai Unik di Setiap Kolom:")
for column in columns_needed:
    print(f"\nKolom {column}:")
    print(filtered_customers_df[column].value_counts().head())

# 5. Memeriksa duplikasi data berdasarkan customer_id dan customer_unique_id
print("\nPemeriksaan Duplikasi Data:")
duplicate_rows = filtered_customers_df.duplicated(subset=['customer_id', 'customer_unique_id']).sum()
print(f"Jumlah duplikasi data berdasarkan 'customer_id' dan 'customer_unique_id': {duplicate_rows}")
