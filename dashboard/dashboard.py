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

df = pd.read_csv('dashboard/main_data.csv', nrows=25000)

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

st.sidebar.header("Informasi Dashboard")
st.sidebar.write("Dashboard ini menampilkan analisis data e-commerce.")

df['year'] = df['order_purchase_timestamp'].dt.year

year_list = sorted(df['year'].unique())
year_options = ["All"] + year_list

selected_year = st.sidebar.selectbox("Pilih Tahun", year_options)

if selected_year != "All":
    df = df[df['year'] == selected_year]

st.write(f"Menampilkan data untuk: {selected_year}")

st.sidebar.markdown("---")
st.sidebar.write("Total Data:", len(df))
st.sidebar.write("Total Pelanggan:", df['customer_unique_id'].nunique())
st.sidebar.write("Total Produk:", df['product_id'].nunique())

col1, col2, col3 = st.columns(3)

col1.metric("Total Transaksi", df['order_id'].nunique())
col2.metric("Total Pelanggan", df['customer_unique_id'].nunique())
col3.metric("Total Produk", df['product_id'].nunique())

product_sales = df.groupby('product_id')['order_item_id'].count().sort_values(ascending=False).head(10)

monthly_orders = df.groupby(df['order_purchase_timestamp'].dt.to_period('M'))['order_id'].nunique()
monthly_orders.index = monthly_orders.index.to_timestamp()

top_customers = df.groupby('customer_unique_id')['order_id'].nunique().sort_values(ascending=False).head(10)

category_sales = df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(10)

st.header("Analisis Produk")

fig1, ax1 = plt.subplots(figsize=(10,5))
product_sales.plot(kind='bar', ax=ax1)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

st.header("Analisis Transaksi")

fig2, ax2 = plt.subplots(figsize=(10,5))
monthly_orders.plot(ax=ax2, marker='o')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

st.header("Analisis Pelanggan")

fig3, ax3 = plt.subplots(figsize=(10,5))
top_customers.plot(kind='bar', ax=ax3)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)

st.header("Kategori Produk")

fig4, ax4 = plt.subplots(figsize=(10,5))
category_sales.plot(kind='bar', ax=ax4)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig4)

st.markdown("---")
st.subheader("Sample Data")
st.dataframe(df.head(10))