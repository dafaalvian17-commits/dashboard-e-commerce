# Dashboard Analisis Data E-Commerce

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data e-commerce guna memahami pola transaksi, perilaku pelanggan, serta performa produk. Analisis dilakukan menggunakan pendekatan Exploratory Data Analysis (EDA) serta teknik analisis lanjutan berupa RFM (Recency, Frequency, Monetary).

## Dataset
Dataset yang digunakan dalam proyek ini merupakan bagian dari E-Commerce Public Dataset, dengan memilih beberapa file yang relevan dengan kebutuhan analisis. Dataset yang digunakan antara lain:

- **orders_dataset.csv**: Berisi informasi terkait transaksi, termasuk waktu pembelian.
- **order_items_dataset.csv**: Berisi detail item dalam setiap transaksi, termasuk jumlah dan produk yang dibeli.
- **customers_dataset.csv**: Berisi informasi pelanggan yang digunakan untuk analisis perilaku pelanggan.
- **products_dataset.csv**: Berisi informasi terkait produk dan kategori produk.

Dataset dipilih berdasarkan relevansi dengan pertanyaan bisnis yang dianalisis, sehingga tidak seluruh dataset digunakan.

## Pertanyaan Bisnis
1. Produk apa yang memiliki penjualan tertinggi berdasarkan total quantity dalam periode dataset yang tersedia?
2. Bagaimana tren jumlah transkasi dari waktu ke waktu berdasarkan tanggal pembelian?
3. Siapa saja pelanggan dengan jumlah transaksi terbanyak selama periode dataset dan bagaimana distribusi aktivitas pembelian mereka?
4. Kategori produk apa yang paling banyak terjual berdasarkan jumlah item yang dibeli oleh pelanggan selama periode dataset?

## Tahapan Analisis
1. Data Gathering  
   Mengumpulkan dataset yang relevan untuk analisis.

2. Data Assessing  
   Melakukan pengecekan terhadap struktur data, tipe data, missing values, serta memahami isi dataset secara keseluruhan.

3. Data Cleaning  
   Membersihkan data dari missing values, duplikasi, serta memastikan tipe data sesuai untuk proses analisis.

4. Exploratory Data Analysis (EDA)  
   Menganalisis pola data melalui visualisasi untuk menjawab pertanyaan bisnis.

5. Analisis RFM  
   - **Recency**: Mengukur waktu sejak transaksi terakhir pelanggan  
   - **Frequency**: Menghitung jumlah transaksi pelanggan  
   - **Monetary**: Menghitung total pengeluaran pelanggan  

6. Visualisasi Data  
   Menyajikan hasil analisis dalam bentuk grafik yang informatif.

7. Pembuatan Dashboard  
   Dashboard interaktif dibuat menggunakan Streamlit untuk menampilkan hasil analisis secara visual.

## Insight Utama
- Sebagian besar pelanggan hanya melakukan satu kali transaksi, yang menunjukkan rendahnya tingkat pembelian ulang.
- Terdapat sebagian kecil pelanggan dengan nilai transaksi tinggi yang berkontribusi besar terhadap total pendapatan.
- Analisis recency menunjukkan adanya pelanggan yang sudah lama tidak melakukan transaksi, sehingga berpotensi mengalami churn.
- Beberapa kategori produk memiliki performa penjualan yang jauh lebih tinggi dibanding kategori lainnya.

## Cara Menjalankan Dashboard

1. Install dependencies:
pip install -r requirements.txt

2. Jalankan aplikasi Streamlit:
streamlit run dashboard/dashboard.py

3. Buka browser dan akses:
http://localhost:8501


## Link Dashboard
Lihat file `url.txt` untuk akses dashboard

## Struktur Folder
submission/
├── dashboard/
│ ├── dashboard.py
│ └── main_data.csv
├── data/
├── submission_proyek_analisis_data.ipynb
├── requirements.txt
├── README.md
└── url.txt

## Author
Muhammad Dafa Alvian Ramadhani  