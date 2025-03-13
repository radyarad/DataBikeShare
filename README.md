# Bike Sharing Analysis & Dashboard by Muhammad Syahradya

Proyek ini berisi **analisis data peminjaman sepeda** dan **dashboard interaktif** menggunakan **Streamlit**.  
Dataset yang digunakan adalah `day.csv` dan `hour.csv`.

## Business Questions
1. **Bagaimana pengaruh musim terhadap pola peminjaman sepeda?**
2. **Apakah terdapat korelasi antara suhu dan jumlah peminjaman sepeda?**

## Tools yang Digunakan
- **Python** (Pandas, Seaborn, Matplotlib)
- **Google Colab** (Analisis dataset)
- **Streamlit** (Dashboard interaktif)

## Dataset
- `day.csv` → Data peminjaman sepeda harian.
- `hour.csv` → Data peminjaman sepeda per jam.

## Cara Menjalankan
### **1. Analisis Dataset di Google Colab**
- **Buka [Google Colab](https://colab.research.google.com/)**.
- **Upload file project `Analisis Dataset Bike Sharing by Muhammad Syahradya.ipynb` dan buka project tersebut**.
- **Upload dataset `day.csv` & `hour.csv` pada project yang sudah dibuka**.
- **Jalankan setiap cell kode Python** untuk melihat insight data.

### **2. Menjalankan Dashboard Streamlit**
1. **Install dependensi**  
   ```bash
   pip install -r requirements.txt
2. **Jalankan Streamlit App**
   ```bash
   streamlit run analisis.py
