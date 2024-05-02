import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import urllib3  # para permitir requests sem bloqueio de SSL


st.set_page_config(layout="wide")

# response = urllib3.request("GET", url, parame)
url = "https://labdados.com/produtos"
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
dados["Data da Compra"] = pd.to_datetime(dados["Data da Compra"], format="%d/%m/%Y")

with st.expander("Colunas"):
    colunas = st.multiselect(
        "Selecione as colunas", list(dados.columns), list(dados.columns)
    )

st.sidebar.title("Filtros")

with st.sidebar.expander("Nome do produto"):
    produtos = st.multiselect(
        "Selecione os produtos", dados["Produto"].unique(), dados["Produto"].unique()
    )
with st.sidebar.expander("preço do produto"):
    preco = st.slider(
        "Selecione o preço",
        dados["Preço"].min(),
        dados["Preço"].max(),
        (dados["Preço"].min(), dados["Preço"].max()),
    )
with st.sidebar.expander("Data da compra"):
    data = st.date_input(
        "Selecione a Data",(dados["Data da Compra"].min(), dados["Data da Compra"].max())
    )

st.dataframe(dados)
