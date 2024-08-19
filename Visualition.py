import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
filtered_customers_df = customers_df[columns_needed]

# 1. Informasi Dasar Dataset
print("Informasi Dasar Dataset:")
print(filtered_customers_df.info())

# 2. Statistik Deskriptif
print("\nStatistik Deskriptif:")
print(filtered_customers_df.describe(include='all'))

# 3. Visualisasi Distribusi Customer Berdasarkan State
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_customers_df, x='customer_state', order=filtered_customers_df['customer_state'].value_counts().index)
plt.title('Distribusi Customer Berdasarkan State')
plt.xlabel('State')
plt.ylabel('Jumlah Customer')
plt.xticks(rotation=45)
plt.show()

# 4. Visualisasi Distribusi Customer Berdasarkan Kota
plt.figure(figsize=(12, 6))
top_10_cities = filtered_customers_df['customer_city'].value_counts().head(10)
sns.barplot(x=top_10_cities.values, y=top_10_cities.index, palette='viridis')
plt.title('10 Kota dengan Jumlah Customer Terbanyak')
plt.xlabel('Jumlah Customer')
plt.ylabel('Kota')
plt.show()

# 5. Visualisasi Distribusi Kode Pos Customer
plt.figure(figsize=(12, 6))
sns.histplot(filtered_customers_df['customer_zip_code_prefix'], bins=30, kde=True)
plt.title('Distribusi Kode Pos Customer')
plt.xlabel('Kode Pos')
plt.ylabel('Frekuensi')
plt.show()

# 6. Analisis Unik Customer ID
unique_customers = filtered_customers_df['customer_unique_id'].nunique()
print(f"\nJumlah Customer Unik: {unique_customers}")

# 7. Analisis Duplikasi Customer ID
duplicate_customers = filtered_customers_df.duplicated(subset=['customer_unique_id']).sum()
print(f"Jumlah Customer Duplikasi: {duplicate_customers}")

# 8. Visualisasi Kode Pos Teratas
print("\nTop 10 Kode Pos dengan Jumlah Customer Terbanyak:")
top_10_zip_codes = filtered_customers_df['customer_zip_code_prefix'].value_counts().head(10)
print(top_10_zip_codes)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_zip_codes.index, y=top_10_zip_codes.values, palette='coolwarm')
plt.title('Top 10 Kode Pos dengan Jumlah Customer Terbanyak')
plt.xlabel('Kode Pos')
plt.ylabel('Jumlah Customer')
plt.show()

# 9. Penjelasan Temuan
print("\nPenjelasan Temuan:")
print("1. Distribusi Customer Berdasarkan State:")
print("   - Grafik ini menunjukkan jumlah customer yang berasal dari setiap state. Beberapa state mungkin memiliki jumlah customer yang sangat besar dibandingkan yang lain.")
print("2. Distribusi Customer Berdasarkan Kota:")
print("   - Grafik ini mengidentifikasi 10 kota dengan jumlah customer terbanyak. Kota-kota ini mungkin menjadi fokus utama dalam strategi pemasaran.")
print("3. Distribusi Kode Pos Customer:")
print("   - Histogram ini menunjukkan variasi dalam kode pos. Jumlah kode pos yang lebih banyak dapat menunjukkan area geografis yang lebih luas atau heterogen.")
print("4. Jumlah Customer Unik:")
print("   - Ini memberi tahu kita berapa banyak customer unik yang tercatat dalam dataset.")
print("5. Jumlah Customer Duplikasi:")
print("   - Jumlah duplikasi dapat menunjukkan masalah dalam pencatatan data atau penggunaan ID yang tidak konsisten.")
print("6. Top 10 Kode Pos Teratas:")
print("   - Menunjukkan kode pos yang paling umum di dataset, yang mungkin berkaitan dengan area pemukiman utama.")