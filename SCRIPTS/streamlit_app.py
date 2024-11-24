import streamlit as st
import requests
import pandas as pd
import plotly.express as px

banco_path = r"C:\Users\Matheus\Documents\Documents\MATHEUS 2k21\FACULDADE\WEB DATA\TRABALHO COMPLETO\TRABALHO\SCRIPTS\banco.db"

from sqlalchemy import create_engine 
engine = create_engine(f'sqlite:///{banco_path}', echo=True)

df_lido = pd.read_sql('SELECT * FROM dados', con=engine)

try:
    with engine.connect() as conn:
        print("Conexão com o banco estabelecida com sucesso!")
except Exception as e:
    print("Erro ao conectar com o banco:", e)

import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM dados")
rows = cursor.fetchall()

for row in rows:
    print(row)


st.write("Dados carregados do banco de dados", df_lido)

st.write("Histograma de Preços")
fig_hist = px.histogram(df_lido.precos) # type: ignore
st.plotly_chart(fig_hist)

st.write("Gráfico de pizza, preços")
fig_pie = px.pie(df_lido, "precos") # type: ignore
st.plotly_chart(fig_pie)

st.write("Barra de Preços")
fig_bar = px.bar(df_lido, 'precos') # type: ignore
st.plotly_chart(fig_bar)

st.write("Barra de Preços por Produto")
fig_bar2 = px.bar(df_lido, x='precos', y='produto', color='agrup1') # type: ignore
st.plotly_chart(fig_bar2)

st.write("Scatter de Preços por Produto")
fig_scar = px.scatter(df_lido, x='precos', y='produto', color='agrup1') # type: ignore
st.plotly_chart(fig_scar)

st.write("Histograma de Preços por Produto")
fig_hist2 = px.histogram(df_lido, x='produto', y='precos', color='agrup1') # type: ignore
st.plotly_chart(fig_hist2)

media = df_lido['precos'].mean()
mediana = df_lido['precos'].median()
desvio_padrao = df_lido['precos'].std()

st.write(f'Média dos Preços: {media:.2f}')
st.write(f'Mediana dos Preços: {mediana:.2f}')
st.write(f'Desvio Padrão dos Preços: {desvio_padrao:.2f}')
