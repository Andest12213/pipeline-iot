import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://postgres:Sbnova-01@localhost:5432/postgres')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Criar o Dashboard
st.title('📊 Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por local
st.header('🌡️ Média de Temperatura por Local')
df_avg_temp = load_data('avg_temp_por_local')
fig1 = px.bar(df_avg_temp, x='local', y='avg_temp', title="Temperatura Média por Local")
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por hora
st.header('⏰ Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem', title="Número de Leituras por Hora")
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('📅 Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], title="Temperaturas Máximas e Mínimas")
st.plotly_chart(fig3)
