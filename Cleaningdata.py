import pandas as pd

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
filtered_customers_df = customers_df[columns_needed]

# 1. Menghapus duplikasi data berdasarkan 'customer_id' dan 'customer_unique_id'
print("Sebelum menghapus duplikasi:")
print(f"Jumlah baris: {filtered_customers_df.shape[0]}")
filtered_customers_df = filtered_customers_df.drop_duplicates(subset=['customer_id', 'customer_unique_id'])
print("Setelah menghapus duplikasi:")
print(f"Jumlah baris: {filtered_customers_df.shape[0]}")

# 2. Mengisi data yang hilang dengan nilai yang sesuai (jika ada)
# Jika terdapat data yang hilang pada 'customer_city' atau 'customer_state', kita bisa mengisi dengan 'Unknown'
filtered_customers_df['customer_city'].fillna('Unknown', inplace=True)
filtered_customers_df['customer_state'].fillna('Unknown', inplace=True)

# 3. Mengoreksi format data jika diperlukan
# Misalnya memastikan bahwa 'customer_zip_code_prefix' adalah string dan bukan integer
filtered_customers_df['customer_zip_code_prefix'] = filtered_customers_df['customer_zip_code_prefix'].astype(str)

# 4. Menghapus baris dengan data yang hilang pada kolom kunci ('customer_id' dan 'customer_unique_id')
filtered_customers_df.dropna(subset=['customer_id', 'customer_unique_id'], inplace=True)

# 5. Menyimpan dataset yang sudah dibersihkan ke file CSV baru
filtered_customers_df.to_csv('cleaned_customers_dataset.csv', index=False)

print("Pembersihan data selesai. Dataset yang bersih telah disimpan ke 'cleaned_customers_dataset.csv'.")