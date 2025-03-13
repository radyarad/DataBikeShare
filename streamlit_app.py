import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("day.csv", delimiter=",")
hour_df = pd.read_csv("hour.csv", delimiter=",")

# Convert season to categorical
season_temp_day = {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'}
day_df['season'] = day_df['season'].map(season_temp_day)
season_temp_hour = {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'}
hour_df['season'] = hour_df['season'].map(season_temp_hour)

# Convert temperature to Celsius
day_df['temp'] = day_df['temp'] * 41
hour_df['temp'] = hour_df['temp'] * 41

# Streamlit App
st.title("Bike Sharing Dashboard")

# Sidebar for filters
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", ['All'] + list(day_df['season'].unique()))
selected_date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [pd.to_datetime(day_df['dteday'].min()), pd.to_datetime(day_df['dteday'].max())])

# Filter data based on selection
if selected_season != 'All':
    day_df = day_df[day_df['season'] == selected_season]
    hour_df = hour_df[hour_df['season'] == selected_season]

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

day_df = day_df[(day_df['dteday'] >= selected_date_range[0]) & (day_df['dteday'] <= selected_date_range[1])]
hour_df = hour_df[(hour_df['dteday'] >= selected_date_range[0]) & (hour_df['dteday'] <= selected_date_range[1])]

# Display filtered data
st.write("### Data yang Difilter")
st.write(day_df)

# Average bike rentals per season
avg_seasonal_day = day_df.groupby('season')['cnt'].mean().reset_index()
avg_seasonal_hour = hour_df.groupby('season')['cnt'].mean().reset_index()

# Correlation between temperature and bike rentals
korelasi_day = day_df['temp'].corr(day_df['cnt'])
korelasi_hour = hour_df['temp'].corr(hour_df['cnt'])

# Visualizations
st.write("### Pengaruh Musim terhadap Jumlah Peminjaman Sepeda")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=avg_seasonal_day, ax=ax1)
ax1.set_title('Pengaruh Musim terhadap Jumlah Peminjaman Sepeda per Musim (day.csv)')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Rata-rata Peminjaman Sepeda')
st.pyplot(fig1)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=avg_seasonal_hour, ax=ax2)
ax2.set_title('Pengaruh Musim terhadap Jumlah Peminjaman Sepeda per Musim (hour.csv)')
ax2.set_xlabel('Musim')
ax2.set_ylabel('Rata-rata Peminjaman Sepeda')
st.pyplot(fig2)

st.write("### Korelasi antara Suhu dan Jumlah Peminjaman Sepeda")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.regplot(x='temp', y='cnt', data=day_df, ax=ax3)
ax3.set_title('Korelasi antara Suhu dan Jumlah Peminjaman Sepeda (day.csv)')
ax3.set_xlabel('Suhu (Celcius)')
ax3.set_ylabel('Jumlah Peminjaman Sepeda')
ax3.grid(True)
st.pyplot(fig3)

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.regplot(x='temp', y='cnt', data=hour_df, ax=ax4)
ax4.set_title('Korelasi antara Suhu dan Jumlah Peminjaman Sepeda (hour.csv)')
ax4.set_xlabel('Suhu (Celcius)')
ax4.set_ylabel('Jumlah Peminjaman Sepeda')
ax4.grid(True)
st.pyplot(fig4)

# Display correlation values
st.write(f"Korelasi antara suhu dan jumlah peminjaman sepeda pada day.csv: {korelasi_day:.2f}")
st.write(f"Korelasi antara suhu dan jumlah peminjaman sepeda pada hour.csv: {korelasi_hour:.2f}")
