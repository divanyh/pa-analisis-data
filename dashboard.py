import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

df_aqi = pd.concat(
    map(pd.read_csv, ['Aotizhongxin.csv', 'Changping.csv', 'Dingling.csv', 'Dongsi.csv',
                      'Guanyuan.csv', 'Gucheng.csv', 'Huairou.csv', 'Nongzhanguan.csv',
                      'Shunyi.csv', 'Tiantan.csv', 'Wanliu.csv', 'Wanshouxigong.csv']), ignore_index=True)

df_date = pd.to_datetime(df_aqi[['year', 'month', 'day']])
df_aqi.insert(6, "date", df_date, True)

# Filter data
min_date = df_aqi["date"].min()
max_date = df_aqi["date"].max()

# def create_bystation_df(df):
#     bystation_df = df.groupby(by="station").agg({
#         'PM2.5': "mean", 'PM10': "mean", 'SO2': "mean", 'NO2': "mean", 'CO': "mean", 'O3': "mean", 'TEMP': "mean", 'PRES': "mean", 'DEWP': "mean", 'RAIN': "mean", 'WSPM': "mean",
#     }).reset_index()
    
#     return bystation_df

with st.sidebar:

    station = st.selectbox(label="Pilih station",
    options=('Aotizhongxin', 'Changping', 'Dingling', 'Dongsi',
                      'Guanyuan', 'Gucheng', 'Huairou', 'Nongzhanguan',
                      'Shunyi', 'Tiantan', 'Wanliu', 'Wanshouxigong')
    )

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# if start_date != end_date:
#     df_aqi = df_aqi.groupby(["date", "region"]).reset_index()    

main_df = df_aqi[(df_aqi["date"] >= str(start_date)) & 
                (df_aqi["date"] <= str(end_date)) 
                & (df_aqi["station"] == station)
                ]

print(main_df.head())

# station_df = create_bystation_df(main_df)

st.header('Air Quality Index :sparkles:')
st.subheader('Daily Report')

hourly_avg_pm25 = main_df.groupby('hour')['PM2.5'].mean().reset_index()

fig,ax = plt.subplots(figsize=(20, 10))
sns.lineplot(x='hour', y='PM2.5', data=hourly_avg_pm25, marker='o')
plt.title('Rata-Rata PM2.5 Sepanjang Hari')
plt.xlabel('Jam')
plt.ylabel('PM2.5 Rata-rata (µg/m³)')
plt.xticks(range(0, 24))
plt.grid(True)

st.pyplot(fig)

st.subheader("Average pollutant ")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="date",y = "PM2.5",
        data=main_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("Kadar PM2.5", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35, labelrotation=45)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="date",y = "PM10",
        data=main_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("Kadar PM10", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35, labelrotation=45)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="date",y = "NO2",
        data=main_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("Kadar NO2", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35, labelrotation=45)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="date",y = "SO2",
        data=main_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("Kadar SO2", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35, labelrotation=45)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="date",y = "CO",
        data=main_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("Kadar CO", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35, labelrotation=45)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="date",y = "O3",
        data=main_df,
        palette=colors,
        ax=ax
    )
    ax.set_title("Kadar O3", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35, labelrotation=45)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)