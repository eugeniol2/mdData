import plotly.express as px
import pandas as pd
import streamlit as st

# Carregar os dados
df = pd.read_csv('agro')




st.write('Csv completo')
st.write(df.head())
st.write(df.describe())

# Lista de siglas dos estados do Nordeste
estados_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

# Filtrar os dados para os estados do Nordeste
df_nordeste = df[df['sigla_uf'].isin(estados_nordeste)]

# Calcular a produção total e a área total para cada cultura no Nordeste por ano
df_nordeste_ano = df_nordeste.groupby('ano').agg({
    'producao_total_arroz': 'sum',
    'producao_total_feijao': 'sum',
    'producao_total_milho': 'sum',
    'producao_total_soja': 'sum',
    'producao_total_algodao': 'sum',
    'producao_total_cana': 'sum',
    'producao_total_trigo': 'sum',
    'area_arroz': 'sum',
    'area_feijao': 'sum',
    'area_milho': 'sum',
    'area_soja': 'sum',
    'area_algodao': 'sum',
    'area_cana': 'sum',
    'area_trigo': 'sum'
}).reset_index()


st.write('Nordeste')
st.write(df_nordeste_ano.head())
st.write(df_nordeste_ano.describe())



# Calcular a produtividade (toneladas por hectare) por ano
df_nordeste_ano['produtividade_arroz'] = df_nordeste_ano['producao_total_arroz'] / df_nordeste_ano['area_arroz']
df_nordeste_ano['produtividade_feijao'] = df_nordeste_ano['producao_total_feijao'] / df_nordeste_ano['area_feijao']
df_nordeste_ano['produtividade_milho'] = df_nordeste_ano['producao_total_milho'] / df_nordeste_ano['area_milho']
df_nordeste_ano['produtividade_soja'] = df_nordeste_ano['producao_total_soja'] / df_nordeste_ano['area_soja']
df_nordeste_ano['produtividade_algodao'] = df_nordeste_ano['producao_total_algodao'] / df_nordeste_ano['area_algodao']
df_nordeste_ano['produtividade_cana'] = df_nordeste_ano['producao_total_cana'] / df_nordeste_ano['area_cana']
df_nordeste_ano['produtividade_trigo'] = df_nordeste_ano['producao_total_trigo'] / df_nordeste_ano['area_trigo']

# Criar um DataFrame para o gráfico de barras de produtividade
df_produtividade = pd.melt(df_nordeste_ano, id_vars=['ano'], value_vars=['produtividade_arroz', 'produtividade_feijao', 'produtividade_milho', 'produtividade_soja', 'produtividade_algodao', 'produtividade_cana', 'produtividade_trigo'], var_name='Cultura', value_name='Produtividade')

# Substituir os nomes das culturas para um formato mais legível
df_produtividade['Cultura'] = df_produtividade['Cultura'].str.replace('produtividade_', '').str.capitalize()

# Criar um DataFrame para o gráfico de torta de área
df_area = pd.melt(df_nordeste_ano, id_vars=['ano'], value_vars=['area_arroz', 'area_feijao', 'area_milho', 'area_soja', 'area_algodao', 'area_cana', 'area_trigo'], var_name='Cultura', value_name='Area')
df_area['Cultura'] = df_area['Cultura'].str.replace('area_', '').str.capitalize()

# Criar um DataFrame para o gráfico de barras de produção total
df_producao_total = pd.melt(df_nordeste_ano, id_vars=['ano'], value_vars=['producao_total_arroz', 'producao_total_feijao', 'producao_total_milho', 'producao_total_soja', 'producao_total_algodao', 'producao_total_cana', 'producao_total_trigo'], var_name='Cultura', value_name='Produção')
df_producao_total['Cultura'] = df_producao_total['Cultura'].str.replace('producao_total_', '').str.capitalize()

# Criar gráficos de barras e torta para cada ano
anos = df_produtividade['ano'].unique()
for ano in anos:
    st.title(f'Análise da Produção Agrícola no Nordeste em {ano}')
    df_ano_produtividade = df_produtividade[df_produtividade['ano'] == ano]
    df_ano_area = df_area[df_area['ano'] == ano]
    df_ano_producao_total = df_producao_total[df_producao_total['ano'] == ano]
    
    # Gráfico de barras de produtividade
    fig_bar_producao_total = px.bar(df_ano_producao_total, x='Cultura', y='Produção', title=f'Produção Total (Toneladas) por Cultura no Nordeste em {ano}', labels={'Cultura': 'Cultura', 'Produção': 'Produção Total (Toneladas)'})
    fig_bar_produtividade = px.bar(df_ano_produtividade, x='Cultura', y='Produtividade', title=f'Produtividade (Toneladas por Hectare) por Cultura no Nordeste em {ano}', labels={'Cultura': 'Cultura', 'Produtividade': 'Produtividade (Toneladas por Hectare)'})
    fig_pie_area = px.pie(df_ano_area, names='Cultura', values='Area', title=f'Área Utilizada por Cultura no Nordeste em {ano}', labels={'Cultura': 'Cultura', 'Area': 'Área (Hectares)'})
  

    st.plotly_chart(fig_bar_producao_total)
    st.plotly_chart(fig_pie_area)
    st.plotly_chart(fig_bar_produtividade)


  

