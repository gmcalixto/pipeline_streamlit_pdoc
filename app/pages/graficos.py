import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def exibir_agrupamento_genero(data):
    """
    Exibe o agrupamento de gênero

    """
    #gerando dataset de agrupamento de genero
    gender_counts = data['gender'].value_counts().rename_axis('gender').reset_index(name='counts')
    gender_counts.set_index('gender', inplace=True)

    #Gráfico do número de pessoas por gênero
    st.divider()
    st.subheader("Número de pessoas por gênero")
    st.bar_chart(gender_counts['counts'], x_label="Gêneros",y_label="Quantidade")



def exibir_agrupamento_geracao(data):
    """
    Exibe o agrupamento de gerações

    """
    #gerando dataset de agrupamento de geração
    generation_counts = data['generation'].value_counts().rename_axis('generation').reset_index(name='counts')
    generation_counts.set_index('generation', inplace=True)

    #Gráfico do número de pessoas por geração (horizontal)
    st.divider()
    st.subheader("Número de pessoas por geração")
    st.bar_chart(generation_counts['counts'], color= "#ffaa00",x_label="Geração",y_label="Quantidade", horizontal=True)


def exibir_media_anos_educacao(data):
    """
    Exibe a média de anos de educação

    """
    #gerando dataset de agrupamento de média de anos de educação por gênero
    gender_education_mean = data.groupby('gender')['years_of_education'].mean().reset_index(name='means')
    gender_education_mean.set_index('gender', inplace=True)

    #Gráfico da média de anos trabalhados
    st.divider()
    st.subheader("Média de anos trabalhados")
    st.bar_chart(gender_education_mean['means'], color= "#00aa00",x_label="Geração",y_label="Média de anos trabalhados")


def exibir_estado_atual_emprego(data):
    """
    Exibe o estado atual de emprego

    """
    #gerando dataset de estado atual de emprego
    job_counts = data['employment_status'].value_counts().rename_axis('employment_status').reset_index(name='counts')
    job_counts.set_index('employment_status', inplace=True)

    #Gráfico de pizza do Status de Emprego no Streamlit com o Plotly
    st.divider()
    st.subheader("Distribuição do Status de Emprego")

    fig = px.pie(job_counts, values='counts', names=job_counts.index)
    st.plotly_chart(fig)



st.title("Gráficos")

if "dataset" in st.session_state:

    exibir_agrupamento_genero(st.session_state['dataset'])

    exibir_agrupamento_geracao(st.session_state['dataset'])

    exibir_media_anos_educacao(st.session_state['dataset'])

    exibir_estado_atual_emprego(st.session_state['dataset'])

else:
    st.info("Dataset não foi carregado")