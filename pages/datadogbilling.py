import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import os
import datetime

st.set_page_config(layout="wide")


def get_time():

    # Get the current date
    current_date = datetime.datetime.now()
    current_month_formatted = current_date.strftime("%Y-%m")
    return current_month_formatted

date_now = get_time()

# Environment variables
api_key = "***"
dd_key = "***"
url = os.environ.get(
    "URL_KEY", "https://api.datadoghq.com/api/v1/usage/billable-summary"
)
date = os.environ.get("DATA_KEY", date_now)

date_format = "?month={}".format(date)
''
headers = {"DD-API-KEY": api_key, "DD-APPLICATION-KEY": dd_key}
response = requests.get(url + date_format, headers=headers)
data = response.json()
usage_billing = data["usage"]

list_org_name = []

# Criando lista de objetos contendo sub_org e consumo de licenças
for usage in usage_billing:
    org_name = usage["org_name"]
    list_org_name.append(org_name)

dados = pd.DataFrame.from_dict(list_org_name)

st.sidebar.title("Filtros")

with st.sidebar.expander("Nome do cliente"):
    cliente = st.multiselect(
        "Selecione os clientes",
        dados[0].unique(),
        dados[0].unique(),
    )

st.dataframe(dados)
