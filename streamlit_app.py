import streamlit as st

# Dados fictícios para os recintos portuários da ABTRA
dados_recintos = [
    {"nome": "Recinto A", "movimentacao": "1500 TEUs", "capacidade": "2000 TEUs", "cidade": "Santos"},
    {"nome": "Recinto B", "movimentacao": "1300 TEUs", "capacidade": "1800 TEUs", "cidade": "Paranaguá"},
    {"nome": "Recinto C", "movimentacao": "1700 TEUs", "capacidade": "2200 TEUs", "cidade": "Rio de Janeiro"},
    {"nome": "Recinto D", "movimentacao": "1200 TEUs", "capacidade": "1600 TEUs", "cidade": "Itajaí"}
]

# Configurações da página
st.set_page_config(page_title="Recintos Portuários da ABTRA", layout="wide")

# Título
st.title("Recintos Portuários da ABTRA")

# Criando 4 colunas de tamanho médio no topo da página
col1, col2, col3, col4 = st.columns(4)

# Preenchendo as colunas com os dados dos recintos
with col1:
    st.subheader(dados_recintos[0]["nome"])
    st.write(f"Movimentação: {dados_recintos[0]['movimentacao']}")
    st.write(f"Capacidade: {dados_recintos[0]['capacidade']}")
    st.write(f"Cidade: {dados_recintos[0]['cidade']}")

with col2:
    st.subheader(dados_recintos[1]["nome"])
    st.write(f"Movimentação: {dados_recintos[1]['movimentacao']}")
    st.write(f"Capacidade: {dados_recintos[1]['capacidade']}")
    st.write(f"Cidade: {dados_recintos[1]['cidade']}")

with col3:
    st.subheader(dados_recintos[2]["nome"])
    st.write(f"Movimentação: {dados_recintos[2]['movimentacao']}")
    st.write(f"Capacidade: {dados_recintos[2]['capacidade']}")
    st.write(f"Cidade: {dados_recintos[2]['cidade']}")

with col4:
    st.subheader(dados_recintos[3]["nome"])
    st.write(f"Movimentação: {dados_recintos[3]['movimentacao']}")
    st.write(f"Capacidade: {dados_recintos[3]['capacidade']}")
    st.write(f"Cidade: {dados_recintos[3]['cidade']}")

# Rodapé ou outras informações adicionais podem ser inseridas aqui
st.write("Dados fornecidos pela ABTRA")
