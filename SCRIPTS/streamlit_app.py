import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine('sqlite:///SCRIPTS/banco.db', echo=True)

try:
    df_lido = pd.read_sql('SELECT * FROM dados', con=engine)
    st.success("Dados carregados do banco com sucesso!")

    st.write("Dados carregados do banco de dados", df_lido)

    st.write("Histograma de Preços")
    fig_hist = px.histogram(df_lido, x='precos')  # Corrigido: especificar x
    st.plotly_chart(fig_hist)

    st.write("Gráfico de pizza, preços")
    fig_pie = px.pie(df_lido, values="precos", names="produto")  # Corrigido
    st.plotly_chart(fig_pie)

    st.write("Barra de Preços")
    fig_bar = px.bar(df_lido, x='produto', y='precos')  # Corrigido
    st.plotly_chart(fig_bar)

    st.write("Barra de Preços por Produto")
    fig_bar2 = px.bar(df_lido, x='precos', y='produto', color='agrup1')
    st.plotly_chart(fig_bar2)

    st.write("Scatter de Preços por Produto")
    fig_scar = px.scatter(df_lido, x='precos', y='produto', color='agrup1')
    st.plotly_chart(fig_scar)

    st.write("Histograma de Preços por Produto")
    fig_hist2 = px.histogram(df_lido, x='produto', y='precos', color='agrup1')
    st.plotly_chart(fig_hist2)

    # Estatísticas
    media = df_lido['precos'].mean()
    mediana = df_lido['precos'].median()
    desvio_padrao = df_lido['precos'].std()

    st.write(f'Média dos Preços: {media:.2f}')
    st.write(f'Mediana dos Preços: {mediana:.2f}')
    st.write(f'Desvio Padrão dos Preços: {desvio_padrao:.2f}')

except Exception as e:
    st.error(f"Erro ao ler os dados do banco: {e}")
