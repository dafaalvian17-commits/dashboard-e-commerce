import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #f5f5f5;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:black;'>Dashboard Analisis E-Commerce</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    import os
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, 'main_data.csv')

    df = pd.read_csv(data_path)
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['year'] = df['order_purchase_timestamp'].dt.year
    return df

df = load_data()
st.sidebar.header("Informasi Dashboard")
st.sidebar.write("Dashboard ini menampilkan analisis data e-commerce.")
st.sidebar.write("Data mencakup transaksi, pelanggan, dan produk.")

min_date = df['order_purchase_timestamp'].min()
max_date = df['order_purchase_timestamp'].max()

start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

df = df[(df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
        (df['order_purchase_timestamp'] <= pd.to_datetime(end_date))]

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

st.header("Analisis Produk")

st.subheader("Top 10 Produk Terlaris")
fig1, ax1 = plt.subplots(figsize=(10,5))
product_sales.plot(kind='bar', ax=ax1)
ax1.set_ylabel("Jumlah Terjual")
ax1.tick_params(axis='x', rotation=45, labelsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig1)

st.markdown("---")

st.header("Analisis Transaksi")

st.subheader("Tren Transaksi")

if (end_date - start_date).days <= 31:
    temp = df.groupby(df['order_purchase_timestamp'].dt.date)['order_id'].nunique()
else:
    temp = df.groupby(df['order_purchase_timestamp'].dt.to_period('M'))['order_id'].nunique()
    temp.index = temp.index.to_timestamp()

fig2, ax2 = plt.subplots(figsize=(10,5))
temp.plot(ax=ax2, marker='o')
ax2.set_ylabel("Jumlah Transaksi")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

st.markdown("---")

st.header("Analisis Pelanggan")

st.subheader("Top 10 Pelanggan")
fig3, ax3 = plt.subplots(figsize=(10,5))
top_customers.plot(kind='bar', ax=ax3)
ax3.set_ylabel("Jumlah Transaksi")
ax3.tick_params(axis='x', rotation=45, labelsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig3)

st.markdown("---")

st.subheader("Top 10 Kategori Produk")
fig4, ax4 = plt.subplots(figsize=(10,5))
category_sales.plot(kind='bar', ax=ax4)
ax4.set_ylabel("Jumlah Terjual")
ax4.tick_params(axis='x', rotation=45, labelsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(fig4)

st.markdown("---")
st.subheader("Sample Data")
st.dataframe(df.head(10))