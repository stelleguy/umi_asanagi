# Proyek Analisis Data
**Langkah-langkah menjalankan dashboard**

## Langkah awal:
1. Install Python v3.13
> [!TIP]
>[link](https://www.python.org/downloads/)
2. Install anaconda3 Distribution v25.11.1
> [!TIP]
>[link](https://www.anaconda.com/download/success?reg=skipped)

## Setup environment:
1. Buka anaconda prompt
2. run
```
conda init cmd.exe
```
3. Setelah selesai, exit
4. Buka file zip proyek ini
5. Extract di suatu folder
6. Masuk ke directory folder tersebut
7. Buka command line/cmd dengan directory folder tersebut
8. run code di bawah satu persatu
```
conda create --name main-ds python=3.13
```
```
conda activate main-ds
```
```
pip install -r requirements.txt
```
```
streamlit run dashboard_ding.py
```
