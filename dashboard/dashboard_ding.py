# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:46:14 2026

@author: GM
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy.stats import chi2_contingency
sns.set(style='dark')

def polutant(df):
    polutant = df[['year', 'month', 'day', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].copy()
    polutant = df.groupby(by = ['year', 'month']).agg({
        "PM2.5" : "mean",
        'PM10' : 'mean',
        'SO2' : 'mean',
        'NO2' : 'mean',
        'CO' : 'mean',
        'O3' : 'mean'}).sort_values(by = ['year', 'month'], ascending = True)
    polutant = polutant.reset_index()
    polutant['time'] = polutant['month'].astype(str)
    return polutant

def parameter(df):
    parameter = df[['year', 'month', 'day', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].copy()
    parameter = df.groupby(by=['year', 'month']).agg({
        "TEMP": "mean",
        'PRES': 'mean',
        'DEWP': 'mean',
        'RAIN': 'mean',
        'WSPM': 'mean'}).sort_values(by=['year', 'month'], ascending = True)
    parameter = parameter.reset_index()
    parameter['time'] = parameter['month'].astype(str)
    return parameter

def polutant_display_pm25(df):
    pm25 = round(df['PM2.5'].mean(), 2)
    with st.container():
        if pm25 <= 15.5:
            st.metric("Rata-rata kadar dan kategori PM2.5:", value= f"{pm25} - Baik")
        elif (pm25 >= 15.6) and (pm25 <= 55.4):
            st.metric("Rata-rata kadar dan kategori PM2.5:", value= f"{pm25} - Sedang")
        elif (pm25 >= 55.5) and (pm25 <= 150.4):
            st.metric("Rata-rata kadar dan kategori PM2.5:", value= f"{pm25} - Tidak sehat")
        elif (pm25 >= 150.5) and (pm25 <= 250.4):
            st.metric("Rata-rata kadar dan kategori PM2.5:", value= f"{pm25} - Sangat tidak sehat")
        else:
            st.metric("Rata-rata kadar dan kategori PM2.5:", value= f"{pm25} - Berbahaya")

def polutant_display_pm10(df):
    pm10 = round(df['PM10'].mean(), 2)
    with st.container():
        if pm10 <= 50:
            st.metric("Rata-rata kadar dan kategori PM10:", value=f"{pm10} - Baik")
        elif (pm10 >= 51) and (pm10 <= 150):
            st.metric("Rata-rata kadar dan kategori PM10:", value=f"{pm10} - Sedang")
        elif (pm10 >= 151) and (pm25 <= 350):
            st.metric("Rata-rata kadar dan kategori PM10:", value=f"{pm10} - Tidak sehat")
        elif (pm10 >= 351) and (pm10 <= 420):
            st.metric("Rata-rata kadar dan kategori PM10:", value=f"{pm10} - Sangat tidak sehat")
        else:
            st.metric("Rata-rata kadar dan kategori PM10:", value=f"{pm10} - Berbahaya")

def polutant_display_lain(df):
    so2 = round(df['SO2'].mean(), 2)
    no2 = round(df['NO2'].mean(), 2)
    co = round(df['CO'].mean(), 2)
    o3 = round(df['O3'].mean(),2)
    with st.container():
        col1, col2 = st.columns(2)
        with col1: 
            st.metric("Kadar SO2: ", value = so2)                
        with col2:
            st.metric("Kadar NO2: ", value = no2)
            
    with st.container():
        col1, col2 = st.columns(2)
        with col1: 
            st.metric("Kadar CO: ", value = co)                
        with col2:
            st.metric("Kadar O3: ", value = o3)


def polutant_graph_pm25(df):
    with st.container():
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(
            df['time'],
            df['PM2.5'],
            marker='o',
            linewidth=1,
            color="#d4493f")
        ax.tick_params(axis='y', labelsize=10)
        ax.tick_params(axis='x', labelsize=10)
        ax.set_ylabel("PM2.5", fontsize=15)
        ax.set_title("Kadar PM2.5", loc="center", fontsize=15)
        st.pyplot(fig)

def polutant_graph_pm10(df):
    with st.container():
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(
            df['time'],
            df['PM10'],
            marker='o',
            linewidth=1,
            color="#32a852")
        ax.tick_params(axis='y', labelsize=10)
        ax.tick_params(axis='x', labelsize=10)
        ax.set_ylabel("PM10", fontsize=15)
        ax.set_title("Kadar PM10", loc="center", fontsize=15)
        st.pyplot(fig)

def polutant_graph_lain(df):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'], 
                df['SO2'], 
                marker='o', 
                linewidth=1, 
                color="#d4493f")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("SO2", fontsize=15)
            ax.set_title("Kadar SO25", loc="center", fontsize=15)
            st.pyplot(fig)
            
        with col2:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'], 
                df['NO2'], 
                marker='o', 
                linewidth=1, 
                color="#32a852")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("NO2", fontsize=15)
            ax.set_title("Kadar NO2", loc="center", fontsize=15)
            st.pyplot(fig)
            
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'], 
                df['CO'],
                marker='o', 
                linewidth=1, 
                color="#d4493f")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("CO", fontsize=15)
            ax.set_title("Kadar CO", loc="center", fontsize=15)
            st.pyplot(fig)
            
        with col2:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'], 
                df['O3'], 
                marker='o', 
                linewidth=1, 
                color="#32a852")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("O3", fontsize=15)
            ax.set_title("Kadar O3", loc="center", fontsize=15)
            st.pyplot(fig)
    
def temppres_graph(df):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'],
                df['TEMP'],
                marker='o',
                linewidth=1,
                color="#39064B")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("TEMP (dalam 'C)", fontsize=15)
            ax.set_title("Suhu", loc="center", fontsize=15)
            st.pyplot(fig)

        with col2:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'],
                df['PRES'],
                marker='o',
                linewidth=1,
                color="#39064B")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("PRES (dalam hPa)", fontsize=15)
            ax.set_title("Tekanan", loc="center", fontsize=15)
            st.pyplot(fig)

def deraws_graph(df):
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'],
                df['DEWP'],
                marker='o',
                linewidth=1,
                color="#39064B")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("DEWP (dalam 'C)", fontsize=15)
            ax.set_title("Titik Embun", loc="center", fontsize=15)
            st.pyplot(fig)

        with col2:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'],
                df['RAIN'],
                marker='o',
                linewidth=1,
                color="#39064B")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("RAIN (dalam mm/min)", fontsize=15)
            ax.set_title("Curah Hujan", loc="center", fontsize=15)
            st.pyplot(fig)

        with col3:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(
                df['time'],
                df['WSPM'],
                marker='o',
                linewidth=1,
                color="#39064B")
            ax.tick_params(axis='y', labelsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.set_ylabel("WSPM (dalam m/s))", fontsize=15)
            ax.set_title("Kecepatan angin", loc="center", fontsize=15)
            st.pyplot(fig)

def wdcount_graph(df):
    with st.container():
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.countplot(
            x = "wd",
            data = df,
            ax = ax
        )
        ax.tick_params(axis = 'x', rotation=45)
        ax.set_ylabel('jumlah')
        ax.set_title('Distribusi arah mata angin pada tahun 2016 di stasiun Dingling')
        st.pyplot(fig)

def scatterreg_graph(df):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.scatter(
                df['TEMP'],
                df['PRES'],
                s = 400,
                alpha = 0.5,
                c = "#60e665",
                marker = 'o',
                edgecolors= "#ed7d53"
            )
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.regplot(
                x = "TEMP",
                y = 'PRES',
                data = df,
                scatter=False,
                ci=95
            )
            ax.set_title("Regression line visualization antara suhu dan tekanan angin tahun 2016 di Stasiun Dingling", fontsize=10)
            st.pyplot(fig)

ding_df = pd.read_csv("ding_2016.csv")
ding_df['date_time'] = pd.to_datetime(ding_df[['year', 'month', 'day']])
ding_df.sort_values(by="date_time", inplace=True)
ding_df.reset_index(inplace=True)
ding_df['date_time'] = pd.to_datetime(ding_df['date_time'], format='%Y-%m-%d')

min_date = ding_df['date_time'].min()
max_date = ding_df['date_time'].max()

#Dashboard utama

st.title("Kualitas udara pada tahun 2016 di Stasiun Dingling")
st.markdown('Data ditampilkan dalam hitungan rata-rata per bulannya sesuai rentang yang dipilih.')

with st.sidebar:
    start_month, end_month = st.date_input(
        label = 'Rentang tanggal:',
        min_value = min_date,
        max_value = max_date,
        value = [min_date, max_date],
        format = "DD/MM/YYYY"
    )

date_start = str(start_month)
date_end = str(end_month)

polutant_edited_df = ding_df[
    (ding_df['date_time'].astype(str) >= date_start) & (ding_df['date_time'].astype(str) <= date_end)
    ]
polutant_edited_df = polutant(polutant_edited_df)

parameter_edited_df = ding_df[
    (ding_df['date_time'].astype(str) >= date_start) & (ding_df['date_time'].astype(str) <= date_end)
    ]
parameter_edited_df = parameter(parameter_edited_df)

wdfreq_df = ding_df[
    (ding_df['date_time'].astype(str) >= date_start) & (ding_df['date_time'].astype(str) <= date_end)
]

with st.expander("Tips"):
    st.write(
        """Silahkan klik tombol persegi di ujung kanan atas grafik untuk membuat grafik muncul full-screen, setelah mengarahkan kursor ke grafik yang ingin dilihat.
        """
    )

st.subheader("Bagaimana tren kadar PM2.5 pada tahun 2016 di Stasiun Dingling?")
polutant_graph_pm25(polutant_edited_df)

st.subheader("Bagaimana tren kadar PM10 pada tahun 2016 di Stasiun Dingling?")
polutant_graph_pm10(polutant_edited_df)

st.subheader("Bagaimana tren kualitas udara mencakup suhu dan tekanan angin pada tahun 2016 di Stasiun Dingling?")
temppres_graph(parameter_edited_df)

st.subheader("Bagaimana kualitas udara seperti titik embun, curah hujan, dan kecepatan angin pada tahun 2016 di Stasiun Dingling?")
deraws_graph(parameter_edited_df)

st.subheader("Bagaimana distribusi arah mata angin pada tahun 2016 di Stasiun Dingling?")
wdcount_graph(wdfreq_df)

st.subheader("Bagaimana status kualitas udara pada tahun 2016 di Stasiun Dingling berdasarkan PM2.5 dan PM10 berdasarkan rentang yang dipilih?")
polutant_display_pm25(polutant_edited_df)
polutant_display_pm10(polutant_edited_df)

st.subheader("Bagaimana hubungan antara suhu dengan tekanan angin pada tahun 2016 di Stasisun Dingling?")
scatterreg_graph(parameter_edited_df)

st.subheader("Tambahan: Polutan tambahan lainnya : SO2, NO2, CO, dan O3.")
polutant_display_lain(polutant_edited_df)
polutant_graph_lain(polutant_edited_df)
