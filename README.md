# Dashboard Analisis Data E-Commerce

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data e-commerce guna memahami pola transaksi, perilaku pelanggan, serta performa produk selama periode Januari 2016 hingga Desember 2018. Analisis dilakukan menggunakan pendekatan Exploratory Data Analysis (EDA) serta analisis lanjutan menggunakan metode RFM (Recency, Frequency, Monetary).

---

## Dataset
Dataset yang digunakan merupakan bagian dari E-Commerce Public Dataset, dengan memilih beberapa file yang relevan dengan kebutuhan analisis, yaitu:

- **orders_dataset.csv** → informasi transaksi dan waktu pembelian  
- **order_items_dataset.csv** → detail item pada setiap transaksi  
- **customers_dataset.csv** → data pelanggan  
- **products_dataset.csv** → informasi produk dan kategori  

Dataset dipilih sesuai dengan kebutuhan analisis sehingga tidak seluruh file digunakan.

---

## Pertanyaan Bisnis
1. Produk apa yang memiliki jumlah penjualan tertinggi berdasarkan total quantity yang terjual pada periode Januari 2016 hingga Desember 2018?  
2. Bagaimana tren jumlah transaksi bulanan berdasarkan jumlah order selama periode Januari 2016 hingga Desember 2018?  
3. Siapa saja pelanggan dengan jumlah transaksi terbanyak berdasarkan jumlah order pada periode Januari 2016 hingga Desember 2018, serta bagaimana perbandingan tingkat aktivitas transaksi di antara pelanggan tersebut?  
4. Kategori produk apa yang memiliki jumlah penjualan tertinggi berdasarkan total item yang terjual pada periode Januari 2016 hingga Desember 2018?  

---

## Tahapan Analisis
1. **Data Gathering**  
   Mengumpulkan dataset yang relevan untuk analisis  

2. **Data Assessing**  
   Mengecek struktur data, tipe data, serta memahami isi dataset  

3. **Data Cleaning**  
   Menangani missing values, duplikasi, dan penyesuaian tipe data  

4. **Exploratory Data Analysis (EDA)**  
   Menganalisis pola data untuk menjawab pertanyaan bisnis  

5. **Analisis RFM**  
   - Recency → waktu sejak transaksi terakhir  
   - Frequency → jumlah transaksi  
   - Monetary → total pengeluaran  

6. **Visualisasi Data**  
   Menyajikan hasil analisis dalam bentuk grafik  

7. **Pembuatan Dashboard**  
   Membuat dashboard interaktif menggunakan Streamlit  

---

## Setup Environment

### Menggunakan Anaconda
conda create --name ecommerce-ds python=3.9  
conda activate ecommerce-ds  
pip install -r requirements.txt  

### Menggunakan Terminal / Shell
pip install pipenv  
pipenv install  
pipenv shell  
pip install -r requirements.txt  

---

## Menjalankan Dashboard
Jalankan perintah berikut pada terminal:

streamlit run dashboard/dashboard.py  

Kemudian buka browser dan akses:

http://localhost:8501  

---

## Link Dashboard
Link dashboard dapat dilihat pada file `url.txt`

---

## Struktur Folder
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
├── submission_proyek_analisis_data.ipynb
├── requirements.txt
├── README.md
└── url.txt

---

## Catatan
Dataset yang digunakan telah melalui proses sampling untuk menyesuaikan batas ukuran file pada GitHub, namun tetap mempertahankan pola utama data sehingga hasil analisis tetap representatif.

---

## Author
Muhammad Dafa Alvian Ramadhani