import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
filtered_customers_df = customers_df[columns_needed]

# 1. Menampilkan informasi dasar tentang dataset
print("Informasi Dasar Dataset:")
print(filtered_customers_df.info())

# 2. Menampilkan beberapa baris pertama dari dataset
print("\nBeberapa Baris Pertama:")
print(filtered_customers_df.head())

# 3. Statistik Deskriptif dari Kolom Numerik
print("\nStatistik Deskriptif:")
print(filtered_customers_df.describe(include='all'))

# 4. Distribusi Customer Berdasarkan State
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_customers_df, x='customer_state', order=filtered_customers_df['customer_state'].value_counts().index)
plt.title('Distribusi Customer Berdasarkan State')
plt.xlabel('State')
plt.ylabel('Jumlah Customer')
plt.xticks(rotation=45)
plt.show()

# 5. Distribusi Customer Berdasarkan Kota
plt.figure(figsize=(12, 6))
top_10_cities = filtered_customers_df['customer_city'].value_counts().head(10)
sns.barplot(x=top_10_cities.values, y=top_10_cities.index, palette='viridis')
plt.title('10 Kota dengan Jumlah Customer Terbanyak')
plt.xlabel('Jumlah Customer')
plt.ylabel('Kota')
plt.show()

# 6. Distribusi customer_zip_code_prefix
plt.figure(figsize=(12, 6))
sns.histplot(filtered_customers_df['customer_zip_code_prefix'], bins=30, kde=True)
plt.title('Distribusi Kode Pos Customer')
plt.xlabel('Kode Pos')
plt.ylabel('Frekuensi')
plt.show()

# 7. Analisis Unik Customer ID
unique_customers = filtered_customers_df['customer_unique_id'].nunique()
print(f"\nJumlah Customer Unik: {unique_customers}")

# 8. Analisis Duplikasi Customer ID
duplicate_customers = filtered_customers_df.duplicated(subset=['customer_unique_id']).sum()
print(f"Jumlah Customer Duplikasi: {duplicate_customers}")

# 9. Analisis Kode Pos Teratas
print("\nTop 10 Kode Pos dengan Jumlah Customer Terbanyak:")
top_10_zip_codes = filtered_customers_df['customer_zip_code_prefix'].value_counts().head(10)
print(top_10_zip_codes)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_zip_codes.index, y=top_10_zip_codes.values, palette='coolwarm')
plt.title('Top 10 Kode Pos dengan Jumlah Customer Terbanyak')
plt.xlabel('Kode Pos')
plt.ylabel('Jumlah Customer')
plt.show()