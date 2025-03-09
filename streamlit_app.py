import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Analisis Data Bike Sharing")
st.write(
    """
    # Muhammad Syahradya mc012d5y2232 App
    App untuk memenuhi submission
    """
)

# Membaca dataset
day_df = pd.read_csv("day.csv", delimiter=",")
hour_df = pd.read_csv("hour.csv", delimiter=",")

# Menampilkan dataset
st.header("Dataset Day")
st.write(day_df)

st.header("Dataset Hour")
st.write(hour_df)

st.write(
    """
    **Insight:**
    - Pada dataset day.csv terdapat 731 baris sebagai hari dan 16 kolom sebagai variabel sedangkan pada dataset hour.csv terdapat 17374 baris sebagai jam per hari dan 17 kolom sebagai variabel (terdapat 1 variabel lebih karena terdapat variabel hr/jam).
    - Kolom - kolom yang relevan terhadap pertanyaan bisnis adalah Season (musim, yang berisi 1: spring, 2: Summer, 3: Fall, dan 4: Winter), temp (temperature atau suhu yang sudah dinormalisasikan), dan cnt (jumlah total peminjaman sepeda).
    """
)


# Cek missing values
st.header("Missing Values")
st.subheader("Missing values pada day_df:")
st.write(day_df.isnull().sum())

st.subheader("Missing values pada hour_df:")
st.write(hour_df.isnull().sum())

# Cek duplikasi data
st.header("Duplikasi Data")
st.write(f"Duplikasi data pada day_df: {day_df.duplicated().sum()}")
st.write(f"Duplikasi data pada hour_df: {hour_df.duplicated().sum()}")

# Cek tipe data
st.header("Tipe Data")
st.subheader("Tipe data pada day_df:")
st.write(day_df.dtypes)

st.subheader("Tipe data pada hour_df:")
st.write(hour_df.dtypes)

st.write(
    """
    **Insight:**
- Pada data day.csv maupun hour.csv tidak memiliki missing values dan data duplikat yang berarti kedua dataset tersebut sudah bersih.
- Tipe data dari data day.csv maupun hour.csv sudah sesuai dengan variabelnya. Contoh variabel yr/tahun bertipe integer dan variabel temp/suhu bertipe float. Hanya saja variabel season yang seharusnya merupakan kategori tetapi pada dataset ini diwakilkan dengan angka.
    """
)

# Mengubah nilai season menjadi kategori
season_temp_day = {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'}
day_df['season'] = day_df['season'].map(season_temp_day)
season_temp_hour = {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'}
hour_df['season'] = hour_df['season'].map(season_temp_hour)

# Melakukan konversi suhu ke skala Celsius
day_df['temp'] = day_df['temp'] * 41
hour_df['temp'] = hour_df['temp'] * 41

# Menghapus kolom yang kurang diperlukan
day_df = day_df.drop(['instant', 'dteday', 'casual', 'registered'], axis=1)
hour_df = hour_df.drop(['instant', 'dteday', 'casual', 'registered', 'hum', 'windspeed', 'atemp'], axis=1)

st.write(
    """
    **Insight:**
    - Seperti yang sudah dikatakan sebelumnya, variabel "season" pada kedua dataset bukan merupakan kategori melainkan integer yang mewakilkan kategori. Maka dari itu dilakukanlah pengubahan nilai pada variabel season menjadi kategori.
    - Seperti yang dikatakan file readme pada kedua dataset tersebut, varibel temp menyimpan nilai suhu dengan derajat celcius yang sudah dinormalisasi dan dibagi dengan 41, maka dari itu dibuatlah penyesuaian yang dimana mengkalikan semua nilai pada variabel temp dengan 41
    - Variabel yang kurang relevan dengan pertanyaan bisnis di drop, tetapi sebenarnya langkah ini tidak diwajibkan.
    """
)

# Menghitung rata-rata peminjaman sepeda per musim
st.header("Rata-rata Peminjaman Sepeda per Musim")
avg_seasonal_day = day_df.groupby('season')['cnt'].mean().reset_index()
st.subheader("Rata-rata peminjaman sepeda per musim (day.csv):")
st.write(avg_seasonal_day)

avg_seasonal_hour = hour_df.groupby('season')['cnt'].mean().reset_index()
st.subheader("Rata-rata peminjaman sepeda per musim (hour.csv):")
st.write(avg_seasonal_hour)


# Menghitung korelasi antara suhu dan jumlah peminjaman sepeda
st.header("Korelasi Suhu dan Jumlah Peminjaman Sepeda")
korelasi_day = day_df['temp'].corr(day_df['cnt'])
st.write(f"Korelasi antara suhu dan jumlah peminjaman sepeda (day.csv): {korelasi_day:.2f}")

korelasi_hour = hour_df['temp'].corr(hour_df['cnt'])
st.write(f"Korelasi antara suhu dan jumlah peminjaman sepeda (hour.csv): {korelasi_hour:.2f}")

st.write(
    """
    **Insight:**
    - Dengan menghitung rata rata peminjaman sepeda per musim, dapat dilihat bahwa pada saat musim fall(musim gugur) peminjaman sepeda lumayan banyak dilakukan, diikuti dengan musim summer (panas), musim winter (dingin), dan paling sedikit di musim spring (semi). Dapat dilihat juga dataset day.csv maupun hour.csv memiliki urutan yang sama. Ini menandakan bahwa musim berpengaruh terhadap banyaknya peminjaman sepedah yang dilakukan
    - Ketika sudah menghitung korelasi antara suhu dan jumlah peminjaman sepeda di kedua dataset, hasil dari perhitungan tersebut keduanya adalah positif yang berarti bahwa suhu dan jumlah peminjaman sepeda memiliki korelasi bersesuaian (positive correllation) sesuai pada modul "Penerapan Dasar-Dasar Descriptive Statistics" bagian "Data Relationship". Pada dataset hour.csv memiliki hasil 0.40477227577865876 yang mendekati 0 atau dapat disebut hampir tidak berkolerasi.
    """
)

# Visualisasi Pengaruh Musim terhadap peminjaman sepeda
st.header("Visualisasi Pengaruh Musim terhadap Peminjaman Sepeda")
st.subheader("Pengaruh Musim (day.csv):")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=avg_seasonal_day, ax=ax1)
ax1.set_title('Pengaruh Musim terhadap Jumlah Peminjaman Sepeda (day.csv)')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Rata-rata Peminjaman Sepeda')
st.pyplot(fig1)

st.subheader("Pengaruh Musim (hour.csv):")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=avg_seasonal_hour, ax=ax2)
ax2.set_title('Pengaruh Musim terhadap Jumlah Peminjaman Sepeda (hour.csv)')
ax2.set_xlabel('Musim')
ax2.set_ylabel('Rata-rata Peminjaman Sepeda')
st.pyplot(fig2)

# Visualisasi korelasi Suhu dengan peminjaman sepeda
st.header("Visualisasi Korelasi Suhu dan Jumlah Peminjaman Sepeda")
st.subheader("Korelasi Suhu (day.csv):")
fig3, ax3 = plt.subplots()
sns.regplot(x='temp', y='cnt', data=day_df, ax=ax3)
ax3.set_title('Korelasi antara Suhu dan Jumlah Peminjaman Sepeda (day.csv)')
ax3.set_xlabel('Suhu (Celcius)')
ax3.set_ylabel('Jumlah Peminjaman Sepeda')
ax3.grid(True)
st.pyplot(fig3)

st.subheader("Korelasi Suhu (hour.csv):")
fig4, ax4 = plt.subplots()
sns.regplot(x='temp', y='cnt', data=hour_df, ax=ax4)
ax4.set_title('Korelasi antara Suhu dan Jumlah Peminjaman Sepeda (hour.csv)')
ax4.set_xlabel('Suhu (Celcius)')
ax4.set_ylabel('Jumlah Peminjaman Sepeda')
ax4.grid(True)
st.pyplot(fig4)

st.write(
    """
    **Insight:**
- Seperti yang sudah dikatakan sebelumnya. Musim terbukti berpengaruh untuk banyaknya peminjaman sepeda. Dengan dibuatnya bar plot, maka dapat lebih mudah melihat perbedaan peminjaman sepeda pada setiap musim. Musim fall (gugur) memiliki rata rata peminjaman sepeda tertinggi sedangkan musim spring (semi) memiliki rata rata peminjaman sepeda terendah. Hal tersebut berlaku untuk kedua dataset day.csv maupun hour.csv 
- Seperti yang sudah dimention sebelumnya, terdapat korelasi antara suhu dan peminjaman sepeda dan hasil dari kolerasi tersebut di ke dua dataset memberikan hasil positif (positive correlation). Dengan dibuatnya scatterplot, kita dapat melihat dengan mudah korelasi antara suhu dan peminjaman sepeda. Semakin tinggi suhu maka orang-orang cenderung lebih sering meminjam sepeda.
    """
)

st.write(
    """
    **Kesimpulan:**
    - Kesimpulan dari pertanyaan 1 yaitu musim terbukti berpengaruh terhadap banyaknya peminjaman sepeda yang dilakukan. Orang-orang cenderung lebih banyak meminjam sepeda pada musim fall (musim gugur) dan cenderung lebih sedikit meminjam sepeda pada musim spring (musim semi). Untuk memudahkan mengetahui perbedaan banyaknya peminjaman per musim maka dapat dilihat pada bar plot dengan rata rata peminjaman sepeda per musimnya yang sudah dibuat sebelumnya.
    - Kesimpulan dari pertanyaan 2 yaitu suhu dan banyaknya peminjaman sepeda terbukti berkolerasi. Dari dataset day.csv maupun hour.csv keduanya menghasilkan nilai kolerasi positif (positive correlation) yang menunjukan bahwa suhu dan banyak peminjaman sepeda memiliki korelasi bersesuaian sesuai dengan modul "Penerapan Dasar-Dasar Descriptive Statistics" bagian "Data Relationship". Untuk mempermudah melihat korelasi antara suhu dan banyaknya peminjaman sepeta, maka dapat melihat scatterplot yang sudah dibuat sebelumnya. Scatter plot tersebut menunjukan tren positif di kedua dataset.
    """
)
