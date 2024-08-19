import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset dari file CSV 
file_path = 'path_to_your_dataset/olist_customers_dataset.csv'
customers_df = pd.read_csv(file_path)

# Memilih kolom yang diinginkan
columns_needed = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']
filtered_customers_df = customers_df[columns_needed]

# Visualisasi Distribusi Customer Berdasarkan Kota
plt.figure(figsize=(12, 6))
top_cities = filtered_customers_df['customer_city'].value_counts().head(10)  # Menampilkan 10 kota teratas
sns.barplot(x=top_cities.values, y=top_cities.index, palette='viridis')
plt.title('10 Kota dengan Jumlah Customer Terbanyak')
plt.xlabel('Jumlah Customer')
plt.ylabel('Kota')
plt.show()

# Menampilkan jumlah customer di setiap kota
print("\nJumlah Customer di Setiap Kota:")
print(filtered_customers_df['customer_city'].value_counts())