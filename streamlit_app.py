import streamlit as st

# Função para estilizar os cartões
def card_style(card_title, card_value, card_color):
    st.markdown(
        f"""
        <div style='background-color: {card_color}; 
                    padding: 20px; 
                    border-radius: 10px;
                    margin: 10px 0;'>
            <h2 style='color: white; text-align: center;'>{card_title}</h2>
            <p style='color: white; text-align: center; font-size: 24px;'>{card_value}</p>
        </div>
        """, unsafe_allow_html=True
    )

# Título do dashboard
st.title("Dashboard de Exemplo com Cartões")

# Layout do dashboard com 4 colunas
col1, col2 = st.columns(2)

# Cartões na primeira coluna
with col1:
    card_style("Usuários Ativos", "1,245", "#1f77b4")
    card_style("Novos Cadastros", "315", "#ff7f0e")

# Cartões na segunda coluna
with col2:
    card_style("Vendas Mensais", "R$ 24,000", "#2ca02c")
    card_style("Visitas no Site", "8,760", "#d62728")

