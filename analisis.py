import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('dataset1_vgsales.csv')

# Data Cleaning
df.drop_duplicates(inplace=True)

# Sidebar
tab = st.sidebar.radio("Pilih Analisis:", [
    "Platform Terlaris", "Genre Terlaris", "Publisher Terbaik", "Tren Penjualan", "Distribusi Regional"])

# Platform Terlaris
if tab == "Platform Terlaris":
    st.title("Platform dengan Penjualan Tertinggi di Setiap Wilayah")
    platform_sales_by_region = df.groupby('Platform')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
    st.bar_chart(platform_sales_by_region)

# Genre Terlaris
elif tab == "Genre Terlaris":
    st.title("Genre Game Paling Laku di Setiap Wilayah")
    genre_sales_by_region = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
    st.bar_chart(genre_sales_by_region)

# Publisher Terbaik
elif tab == "Publisher Terbaik":
    st.title("Top 10 Publisher Berdasarkan Global Sales")
    top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_publishers.values, y=top_publishers.index)
    plt.xlabel("Total Penjualan (Juta)")
    st.pyplot(plt)

# Tren Penjualan
elif tab == "Tren Penjualan":
    st.title("Tren Penjualan Game Berdasarkan Tahun Rilis")
    sales_by_year = df.groupby('Year')['Global_Sales'].sum()
    plt.figure(figsize=(10, 4))
    plt.plot(sales_by_year.index, sales_by_year.values, marker='o')
    plt.xlabel("Tahun Rilis")
    plt.ylabel("Penjualan Global (Juta)")
    plt.grid()
    st.pyplot(plt)

# Distribusi Regional
elif tab == "Distribusi Regional":
    st.title("Distribusi Penjualan Berdasarkan Wilayah")
    total_na_sales = df['NA_Sales'].sum()
    total_eu_sales = df['EU_Sales'].sum()
    total_jp_sales = df['JP_Sales'].sum()
    total_other_sales = df['Other_Sales'].sum()
    region_sales = [total_na_sales, total_eu_sales, total_jp_sales, total_other_sales]
    regions = ['North America', 'Europe', 'Japan', 'Other']
    fig, ax = plt.subplots()
    ax.pie(region_sales, labels=regions, autopct='%1.1f%%', startangle=140)
    plt.title("Persentase Penjualan Berdasarkan Wilayah")
    st.pyplot(fig)
