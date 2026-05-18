# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:46:14 2026

@author: GM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def polutant_df(df, opt):
    polutant_df = df[['year', 'month', 'day', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].copy()
    
    if opt == 'daily':
        polutant_df = df.groupby(by = ['year', 'month', 'day']).agg({
            "PM2.5" : "mean",
            'PM10' : 'mean',
            'SO2' : 'mean',
            'NO2' : 'mean',
            'CO' : 'mean',
            'O3' : 'mean'}).sort_values(by = ['year', 'month', 'day'], ascending = True)
        polutant_df = polutant_df.reset_index()
        polutant_df['time'] = polutant_df['year'].astype(str) + '/' + polutant_df['month'].astype(str) + '/' + polutant_df['day'].astype(str) 
        
    elif opt == 'monthly':
        polutant_df = df.groupby(by = ['year', 'month']).agg({
            "PM2.5" : "mean",
            'PM10' : 'mean',
            'SO2' : 'mean',
            'NO2' : 'mean',
            'CO' : 'mean',
            'O3' : 'mean'}).sort_values(by = ['year', 'month'], ascending = True)
        polutant_df = polutant_df.reset_index()
        polutant_df['time'] = polutant_df['year'].astype(str) + '/' + polutant_df['month'].astype(str)
        
    else:
        polutant_df = df.groupby(by = ['year']).agg({
            "PM2.5" : "mean",
            'PM10' : 'mean',
            'SO2' : 'mean',
            'NO2' : 'mean',
            'CO' : 'mean',
            'O3' : 'mean'}).sort_values(by = ['year'], ascending = True)
        polutant_df = polutant_df.reset_index()
        polutant_df['time'] = polutant_df['year'].astype(str)
   
    return polutant_df

def polutant_display(df):
    pm25 = round(df['PM2.5'].mean(), 2)
    pm10 = round(df['PM10'].mean(), 2)
    so2 = round(df['SO2'].mean(), 2)
    no2 = round(df['NO2'].mean(), 2)
    co = round(df['CO'].mean(), 2)
    o3 = round(df['O3'].mean(),2)
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1: 
            if pm25 <= 15.5:
                st.metric("Kadar dan Kategori PM2.5:", value= f"{pm25} - Baik")
            elif (pm25 >= 15.6) and (pm25 <= 55.4):
                st.metric("Kadar dan Kategori PM2.5:", value= f"{pm25} - Sedang")
            elif (pm25 >= 55.5) and (pm25 <= 150.4):
                st.metric("Kadar dan Kategori PM2.5:", value= f"{pm25} - Tidak sehat")
            elif (pm25 >= 150.5) and (pm25 <= 250.4):
                st.metric("Kadar dan Kategori PM2.5:", value= f"{pm25} - Sangat tidak sehat")
            else:
                st.metric("Kadar dan Kategori PM2.5:", value= f"{pm25} - Berbahaya")
                
        with col2:
            if pm10 <= 50:
                st.metric("Kadar dan Kategori PM10:", value= f"{pm10} - Baik")
            elif (pm10 >= 51) and (pm10 <= 150):
                st.metric("Kadar dan Kategori PM10:", value= f"{pm10} - Sedang")
            elif (pm10 >= 151) and (pm25 <= 350):
                st.metric("Kadar dan Kategori PM10:", value= f"{pm10} - Tidak sehat")
            elif (pm10 >= 351) and (pm10 <= 420):
                st.metric("Kadar dan Kategori PM10:", value= f"{pm10} - Sangat tidak sehat")
            else:
                st.metric("Kadar dan Kategori PM10:", value= f"{pm10} - Berbahaya")
                
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
            
def polutant_graph(df):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
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
            
        with col2:
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
    
ding_df = pd.read_csv("ding.csv")
ding_df['date_time'] = pd.to_datetime(ding_df[['year', 'month', 'day']])
ding_df.sort_values(by="date_time", inplace=True)
ding_df.reset_index(inplace=True)
ding_df['date_time'] = pd.to_datetime(ding_df['date_time'], format='%Y-%m-%d')

min_date = ding_df['date_time'].min()
max_date = ding_df['date_time'].max()

#Dashboard utama

st.title("Kualitas udara di Stasiun Dingling berdasarkan enam jenis polutan")
st.subheader("Terdapat enam polutan yang tertulis di Stasiun Dingling: PM2.5, PM10, SO2, NO2, CO, dan O3.")
with st.sidebar:
    opt = st.selectbox("Rentang waktu: ", ('daily', 'monthly', 'yearly'))
    
if opt == 'daily':
    with st.sidebar:
        start_date, end_date = st.date_input(
            label = 'Rentang tanggal:',
            min_value = min_date,
            max_value = max_date,
            value = [min_date, max_date]
        )
    
    date_start = str(start_date)
    date_end = str(end_date)
    
    polutant_edited_df = ding_df[
        (ding_df['date_time'].astype(str) >= date_start) & (ding_df['date_time'].astype(str) <= date_end)
        ]
    polutant_edited_df_2 = polutant_df(polutant_edited_df, opt)
    
    st.header("Polutan udara di Stasiun Dingling Harian")
    polutant_display(polutant_edited_df_2)
    with st.expander("Tips"):
        st.write(
            """Silahkan klik tombol persegi di ujung kanan atas grafik untuk membuat grafik muncul full-screen, setelah mengarahkan kursor ke grafik yang ingin dilihat.
            """
            )
    polutant_graph(polutant_edited_df_2)
        
elif opt == 'monthly':
    with st.sidebar:
        start_month, end_month = st.date_input(
            label = 'Rentang tanggal:',
            min_value = min_date,
            max_value = max_date,
            value = [min_date, max_date]
        )
    
    date_start = str(start_month)
    date_end = str(end_month)
    
    polutant_edited_df = ding_df[
        (ding_df['date_time'].astype(str) >= date_start) & (ding_df['date_time'].astype(str) <= date_end)
        ]
    polutant_edited_df_2 = polutant_df(polutant_edited_df, opt)
    
    st.header("Polutan udara di Stasiun Dingling Bulanan")
    polutant_display(polutant_edited_df_2)
    with st.expander("Tips"):
        st.write(
            """Silahkan klik tombol persegi di ujung kanan atas grafik untuk membuat grafik muncul full-screen, setelah mengarahkan kursor ke grafik yang ingin dilihat.
            """
            )
    polutant_graph(polutant_edited_df_2)
        
else:
    with st.sidebar:
        start_year, end_year = st.date_input(
            label = 'Rentang tanggal:',
            min_value = min_date,
            max_value = max_date,
            value = [min_date, max_date]
        )
    
    date_start = str(start_year)
    date_end = str(end_year)
    
    polutant_edited_df = ding_df[
        (ding_df['date_time'].astype(str) >= date_start) & (ding_df['date_time'].astype(str) <= date_end)
        ]
    polutant_edited_df_2 = polutant_df(polutant_edited_df, opt)
    
    st.header("Polutan udara di Stasiun Dingling Tahunan")
    polutant_display(polutant_edited_df_2)
    with st.expander("Tips"):
        st.write(
            """Silahkan klik tombol persegi di ujung kanan atas grafik untuk membuat grafik muncul full-screen, setelah mengarahkan kursor ke grafik yang ingin dilihat.
            """
            )
    polutant_graph(polutant_edited_df_2)