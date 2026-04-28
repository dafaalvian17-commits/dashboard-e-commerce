import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #f5f5f5;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

st.title("Dashboard Analisis E-Commerce")

@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "main_data.csv")

    df = pd.read_csv(data_path)

    df = df[
        [
            "order_id",
            "customer_unique_id",
            "product_id",
            "order_item_id",
            "order_purchase_timestamp",
            "product_category_name",
        ]
    ]

    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

    return df


df = load_data()

min_date = df["order_purchase_timestamp"].min()
max_date = df["order_purchase_timestamp"].max()

st.sidebar.header("Filter Tanggal")

start_date = st.sidebar.date_input("Start Date", min_date.date())
end_date = st.sidebar.date_input("End Date", max_date.date())

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

if start_date > end_date:
    st.error("Start date harus sebelum end date")
    st.stop()

df = df[
    (df["order_purchase_timestamp"] >= start_date)
    & (df["order_purchase_timestamp"] <= end_date)
]

if df.empty:
    st.warning("Tidak ada data pada rentang tanggal ini")
    st.stop()

st.sidebar.markdown("---")
st.sidebar.write("Total Data:", len(df))
st.sidebar.write("Total Pelanggan:", df["customer_unique_id"].nunique())
st.sidebar.write("Total Produk:", df["product_id"].nunique())

col1, col2, col3 = st.columns(3)

col1.metric("Total Transaksi", df["order_id"].nunique())
col2.metric("Total Pelanggan", df["customer_unique_id"].nunique())
col3.metric("Total Produk", df["product_id"].nunique())

product_sales = (
    df.groupby("product_id")["order_item_id"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

top_customers = (
    df.groupby("customer_unique_id")["order_id"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

category_sales = (
    df.groupby("product_category_name")["order_item_id"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

st.header("Analisis Produk")

fig1, ax1 = plt.subplots(figsize=(10, 5))
product_sales.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Jumlah Terjual")
ax1.tick_params(axis="x", rotation=45, labelsize=8)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
st.pyplot(fig1)

st.header("Analisis Transaksi")

if (end_date - start_date).days <= 31:
    transaksi = df.groupby(df["order_purchase_timestamp"].dt.date)[
        "order_id"
    ].nunique()
else:
    transaksi = df.groupby(
        df["order_purchase_timestamp"].dt.to_period("M")
    )["order_id"].nunique()
    transaksi.index = transaksi.index.to_timestamp()

fig2, ax2 = plt.subplots(figsize=(10, 5))
transaksi.plot(ax=ax2, marker="o")
ax2.set_ylabel("Jumlah Transaksi")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

st.header("Analisis Pelanggan")

fig3, ax3 = plt.subplots(figsize=(10, 5))
top_customers.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Jumlah Transaksi")
ax3.tick_params(axis="x", rotation=45, labelsize=8)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
st.pyplot(fig3)

st.header("Kategori Produk")

fig4, ax4 = plt.subplots(figsize=(10, 5))
category_sales.plot(kind="bar", ax=ax4)
ax4.set_ylabel("Jumlah Terjual")
ax4.tick_params(axis="x", rotation=45, labelsize=8)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
st.pyplot(fig4)

st.markdown("---")
st.subheader("Sample Data")
st.dataframe(df.head(10))