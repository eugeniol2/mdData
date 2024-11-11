import plotly.express as px
import pandas as pd
import streamlit as st

# Carregar os dados
df = pd.read_csv('agro')

# Lista de colunas a verificar
colunas_a_verificar = ["producao_cafe", "area_cafe", "quantidade_estabelecimentos_cafe", "valor_total_producao_cafe", "despesa_adubos", "despesa_defensivos", "despesa_sementes", "quantidade_estabelecimentos", "area_total", "quantidade_tratores", "quantidade_maquinas_plantio", "quantidade_maquina_colheita", "areas_irrigacao", "numero_estabelecimentos_cooperativas", "area_soja", "area_milho", "producao_total_soja", "producao_total_milho", "numero_estabelecimentos_total", "pessoal_ocupado_total", "pessoal_ocupado_parentesco_produtor", "pessoal_14_mais_sem_parentesco", "valor_producao_total", "valor_total_producao_animal_grande", "valor_total_producao_vegetal", "valor_total_producao_hortifruti", "valor_total_producao_silvicultura", "valor_total_producao_aves", "area_arroz", "area_feijao", "area_milho", "area_mandioca", "area_soja", "producao_total_arroz", "producao_total_feijao", "producao_total_milho", "producao_total_mandioca", "producao_total_soja", "valor_total_arroz", "valor_total_feijao", "valor_total_milho", "valor_total_mandioca", "valor_total_soja", "despesa_arrendamentos", "despesa_salarios", "numero_estabelecimentos_proprietario", "numero_estabelecimentos_arrendatario", "numero_estabelecimentos_ocupantes"]

# Verificar se as colunas existem e possuem dados
dados_colunas = []
for coluna in colunas_a_verificar:
    if coluna in df.columns:
        valores_nao_nulos = df[coluna].notnull().sum()
        dados_colunas.append([coluna, 'Sim', valores_nao_nulos])
    else:
        dados_colunas.append([coluna, 'Não', 0])

# Criar um DataFrame com as informações das colunas
df_colunas = pd.DataFrame(dados_colunas, columns=['Coluna', 'Existe', 'Valores Não Nulos'])

# Exibir o DataFrame como uma tabela
st.write('Informações das Colunas')
st.dataframe(df_colunas)

# Obter os nomes das colunas
colunas = df.columns.tolist()
st.write('Nomes das colunas:')
st.write(colunas)

# Obter os valores de cada coluna
for coluna in colunas:
    st.write(f'Valores da coluna {coluna}:')
    st.write(df[coluna].tolist())