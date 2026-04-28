import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")

st.title("Dashboard Analisis E-Commerce")


df = pd.read_csv('dashboard/main_data.csv')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])


st.sidebar.header("Informasi Dashboard")

st.sidebar.write("""
Dashboard ini menampilkan analisis data e-commerce yang meliputi:
- Produk terlaris
- Tren transaksi
- Pelanggan paling aktif
- Kategori produk terlaris

Gunakan filter tanggal untuk melihat perubahan data dalam periode tertentu.
""")

st.sidebar.markdown("---")

min_date = df['order_purchase_timestamp'].min()
max_date = df['order_purchase_timestamp'].max()

start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

df = df[
    (df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
    (df['order_purchase_timestamp'] <= pd.to_datetime(end_date))
]

st.sidebar.markdown("---")
st.sidebar.write("Total Data:", len(df))
st.sidebar.write("Total Pelanggan:", df['customer_unique_id'].nunique())
st.sidebar.write("Total Produk:", df['product_id'].nunique())


col1, col2, col3 = st.columns(3)

col1.metric("Total Transaksi", df['order_id'].nunique())
col2.metric("Total Pelanggan", df['customer_unique_id'].nunique())
col3.metric("Total Produk", df['product_id'].nunique())


product_sales = df.groupby('product_id')['order_item_id'].count().sort_values(ascending=False).head(10)

top_customers = df.groupby('customer_unique_id')['order_id'].nunique().sort_values(ascending=False).head(10)

category_sales = df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(10)


date_range = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days

if date_range <= 60:
    orders = df.groupby(df['order_purchase_timestamp'].dt.date)['order_id'].nunique()
    x_label = "Tanggal (Harian)"
else:
    orders = df.groupby(df['order_purchase_timestamp'].dt.to_period('M'))['order_id'].nunique()
    orders.index = orders.index.to_timestamp()
    x_label = "Bulan"


st.header("Analisis Produk")

fig1, ax1 = plt.subplots(figsize=(8,4))
product_sales.plot(kind='bar', ax=ax1)
ax1.set_ylabel("Jumlah Terjual")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig1)


st.header("Analisis Transaksi")

fig2, ax2 = plt.subplots(figsize=(8,4))
orders.plot(ax=ax2, marker='o')
ax2.set_ylabel("Jumlah Transaksi")
ax2.set_xlabel(x_label)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig2)


st.header("Analisis Pelanggan")

fig3, ax3 = plt.subplots(figsize=(8,4))
top_customers.plot(kind='bar', ax=ax3)
ax3.set_ylabel("Jumlah Transaksi")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig3)


st.header("Kategori Produk")

fig4, ax4 = plt.subplots(figsize=(8,4))
category_sales.plot(kind='bar', ax=ax4)
ax4.set_ylabel("Jumlah Terjual")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig4)


st.markdown("---")
st.subheader("Sample Data")
st.dataframe(df.head(10))