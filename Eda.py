import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
filtered_customers_df = customers_df[columns_needed]

# 1. Informasi dasar tentang dataset
print("Informasi Dasar Dataset:")
print(filtered_customers_df.info())

# 2. Distribusi customer berdasarkan state
print("\nDistribusi Customer Berdasarkan State:")
print(filtered_customers_df['customer_state'].value_counts())

plt.figure(figsize=(10,6))
sns.countplot(data=filtered_customers_df, x='customer_state', order=filtered_customers_df['customer_state'].value_counts().index)
plt.title('Distribusi Customer Berdasarkan State')
plt.xlabel('State')
plt.ylabel('Jumlah Customer')
plt.xticks(rotation=45)
plt.show()

# 3. Distribusi customer berdasarkan kota
print("\nDistribusi Customer Berdasarkan Kota:")
print(filtered_customers_df['customer_city'].value_counts().head(10))  # Menampilkan 10 kota teratas

plt.figure(figsize=(10,6))
sns.countplot(data=filtered_customers_df, y='customer_city', order=filtered_customers_df['customer_city'].value_counts().head(10).index)
plt.title('10 Kota dengan Jumlah Customer Terbanyak')
plt.xlabel('Jumlah Customer')
plt.ylabel('Kota')
plt.show()

# 4. Analisis customer_zip_code_prefix
print("\nAnalisis customer_zip_code_prefix:")
print(filtered_customers_df['customer_zip_code_prefix'].describe())

plt.figure(figsize=(10,6))
sns.histplot(filtered_customers_df['customer_zip_code_prefix'], bins=30, kde=True)
plt.title('Distribusi Kode Pos Customer')
plt.xlabel('customer_zip_code_prefix')
plt.ylabel('Frekuensi')
plt.show()

# 5. Analisis Unik Customer ID
unique_customers = filtered_customers_df['customer_unique_id'].nunique()
print(f"\nJumlah Customer Unik: {unique_customers}")

# 6. Analisis Duplikasi Customer ID
duplicate_customers = filtered_customers_df.duplicated(subset=['customer_unique_id']).sum()
print(f"Jumlah Customer Duplikasi: {duplicate_customers}")