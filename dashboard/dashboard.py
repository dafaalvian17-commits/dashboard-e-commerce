import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CONFIG & STYLE

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

# LOAD DATA

df = pd.read_csv('dashboard/main_data.csv')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# SIDEBAR

st.sidebar.header("Informasi Dashboard")
st.sidebar.write("Dashboard ini menampilkan analisis data e-commerce.")
st.sidebar.write("Data mencakup transaksi, pelanggan, dan produk.")

# FILTER TAHUN
df['year'] = df['order_purchase_timestamp'].dt.year

year_list = sorted(df['year'].unique())
year_options = ["All"] + year_list

selected_year = st.sidebar.selectbox(
    "Pilih Tahun",
    year_options
)

if selected_year != "All":
    df = df[df['year'] == selected_year]

st.write(f"Menampilkan data untuk: {selected_year}")
st.sidebar.markdown("---")
st.sidebar.write("Total Data:", len(df))
st.sidebar.write("Total Pelanggan:", df['customer_unique_id'].nunique())
st.sidebar.write("Total Produk:", df['product_id'].nunique())

# METRIC (KPI)

col1, col2, col3 = st.columns(3)

col1.metric("Total Transaksi", df['order_id'].nunique())
col2.metric("Total Pelanggan", df['customer_unique_id'].nunique())
col3.metric("Total Produk", df['product_id'].nunique())

# HITUNG DATA

product_sales = df.groupby('product_id')['order_item_id'].count().sort_values(ascending=False).head(10)

monthly_orders = df.groupby(df['order_purchase_timestamp'].dt.to_period('M'))['order_id'].nunique()
monthly_orders.index = monthly_orders.index.to_timestamp()

top_customers = df.groupby('customer_unique_id')['order_id'].nunique().sort_values(ascending=False).head(10)

category_sales = df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(10)

# VISUALISASI

st.header("Analisis Produk")

st.subheader("Top 10 Produk Terlaris")
fig1, ax1 = plt.subplots(figsize=(12,6))
product_sales.plot(kind='bar', ax=ax1)
ax1.set_title("Top Produk")
ax1.set_ylabel("Jumlah Terjual")
ax1.set_xlabel("")
ax1.tick_params(axis='x', rotation=45, labelsize=8)
for label in ax1.get_xticklabels():
    label.set_horizontalalignment('right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig1)

st.markdown("---")

st.header("Analisis Transaksi")

st.subheader("Tren Transaksi")
fig2, ax2 = plt.subplots(figsize=(12,6))
monthly_orders.plot(ax=ax2)
ax2.set_title("Tren Bulanan")
ax2.set_ylabel("Jumlah Transaksi")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig2)

st.markdown("---")

st.header("Analisis Pelanggan")

st.subheader("Top 10 Pelanggan")
fig3, ax3 = plt.subplots(figsize=(12,6))
top_customers.plot(kind='bar', ax=ax3)
ax3.set_title("Pelanggan Teraktif")
ax3.set_ylabel("Jumlah Transaksi")
ax3.set_xlabel("")
ax3.tick_params(axis='x', rotation=45, labelsize=8)
for label in ax3.get_xticklabels():
    label.set_horizontalalignment('right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig3)

st.markdown("---")

st.subheader("Top 10 Kategori Produk")
fig4, ax4 = plt.subplots(figsize=(12,6))
category_sales.plot(kind='bar', ax=ax4)
ax4.set_title("Kategori Terlaris")
ax4.set_ylabel("Jumlah Terjual")
ax4.set_xlabel("")
ax4.tick_params(axis='x', rotation=45, labelsize=8)
for label in ax4.get_xticklabels():
    label.set_horizontalalignment('right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig4)

# SAMPLE DATA

st.markdown("---")
st.subheader("Sample Data")
st.dataframe(df.head(10))