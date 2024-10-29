import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def dados_origem(data):
    """
    Mostra os dados de origem CSV em uma tabela

    """
    st.subheader("Dados de origem")
    st.dataframe(data)


#configurando o titulo da janela
st.set_page_config(page_title="Indicadores referente ao arquivo CSV", page_icon="👁")

try:
    #abre o arquivo manualmente
    file = 'persons.csv'
    st.session_state['dataset'] = pd.read_csv(file)

except Exception as e:
    st.info("Arquino não encontrado")


#renderizações no Streamlit
st.title("Indicadores referente ao arquivo CSV")

if "dataset" in st.session_state:

    dados_origem(st.session_state['dataset'])

else:
    st.info("Dataset não foi carregado com sucesso")

