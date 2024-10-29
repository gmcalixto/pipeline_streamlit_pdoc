import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



def distribuicao_geral_idade(data):
    """
    Gera a distribuição geral de idades

    """

    # Criar faixas etárias
    data['age_group'] = pd.cut(data['age'], bins=[0, 18, 30, 45, 60, 100], labels=['0-18', '19-30', '31-45', '46-60', '61+'])

    #distribuição geral por idade
    age_group_counts = data['age_group'].value_counts().sort_index()

    #Mostra o histograma geral de idades
    st.divider()
    st.subheader("Distribuição por Idade")
    # Criando o gráfico de barras agrupadas
    fig_grouped_age = px.bar(age_group_counts,
                        labels={"value": "Número de Pessoas", "variable": "Idade"}, 
                        barmode='stack')

    fig_grouped_age.update_layout(
        xaxis_title="Idades"
    )

    st.plotly_chart(fig_grouped_age)


def distribuicao_gerero_idade(data):

    """
    Gera a distribuição por gênero e idades

    """

    #distribuição por gênero e por idade
    age_gender_distribution = data.groupby(['age_group', 'gender'], observed=True).size().unstack(fill_value=0)

    #Mostra o histograma geral de idades agrupado por gênero
    st.divider()
    st.subheader("Distribuição por Idade e Gênero")
    # Criando o gráfico de barras agrupadas
    fig_grouped_gen = px.bar(age_gender_distribution,
                        labels={"value": "Número de Pessoas", "variable": "Idade"}, 
                        barmode='group')

    fig_grouped_gen.update_layout(
        xaxis_title="Idades"
    )

    st.plotly_chart(fig_grouped_gen)




st.title("Histograma")

if "dataset" in st.session_state:

    distribuicao_geral_idade(st.session_state['dataset'])

    distribuicao_gerero_idade(st.session_state['dataset'])

else:
    st.info("Dicionario não foi carregado")

