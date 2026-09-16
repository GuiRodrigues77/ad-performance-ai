import pandas as pd
import streamlit as st
import plotly.express as px

from src.metrics import calculate_metrics
from src.ai_analysis import analisar_campanha


st.set_page_config(
    page_title="AdPerformance AI",
    layout="wide"
)

st.title("📊 AdPerformance AI")
st.write("Dashboard para análise automatizada de campanhas de tráfego pago.")

st.sidebar.title("🔎 Filtros")

filtro_classificacao = st.sidebar.selectbox(
    "Classificação",
    [
        "Todas",
        "Excelente",
        "Boa",
        "Atenção",
        "Baixo desempenho"
    ]
)

arquivo = st.file_uploader(
    "Envie um arquivo CSV de campanhas",
    type=["csv"]
)

if arquivo is not None:
    df = pd.read_csv(arquivo)
else:
    df = pd.read_csv("data/campanhas.csv")

df = calculate_metrics(df)

def classificar_campanha(row):
    if row["ROAS"] >= 3 and row["CPA"] <= 20:
        return "Excelente"
    elif row["ROAS"] >= 2:
        return "Boa"
    elif row["ROAS"] >= 1:
        return "Atenção"
    else:
        return "Baixo desempenho"


df["Classificacao"] = df.apply(classificar_campanha, axis=1)

if filtro_classificacao != "Todas":
    df = df[df["Classificacao"] == filtro_classificacao]

def gerar_recomendacao(row):
    if row["ROAS"] >= 3 and row["CPA"] <= 20:
        return "Manter campanha e considerar aumento gradual do investimento."
    elif row["ROAS"] >= 2:
        return "Campanha com bom desempenho. Monitorar e buscar otimizações."
    elif row["ROAS"] >= 1:
        return "Revisar público, criativo e orçamento."
    else:
        return "Avaliar pausa da campanha e investigar os principais problemas."


df["Recomendacao"] = df.apply(gerar_recomendacao, axis=1)

st.subheader("Visão geral")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Investimento",
    f"R$ {df['investimento'].sum():,.2f}"
)

col2.metric(
    "Cliques",
    f"{df['cliques'].sum():,}"
)

col3.metric(
    "Conversões",
    f"{df['conversoes'].sum():,}"
)

col4.metric(
    "Receita",
    f"R$ {df['receita'].sum():,.2f}"
)

st.subheader("Campanhas")

st.dataframe(
    df,
    use_container_width=True
)

st.subheader("ROAS por campanha")

fig = px.bar(
    df,
    x="campanha",
    y="ROAS",
    title="Retorno sobre investimento por campanha"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("Classificação das campanhas")

classificacao = df["Classificacao"].value_counts().reset_index()
classificacao.columns = ["Classificacao", "Quantidade"]

fig_classificacao = px.pie(
    classificacao,
    names="Classificacao",
    values="Quantidade",
    title="Distribuição das campanhas por desempenho"
)

st.plotly_chart(
    fig_classificacao,
    use_container_width=True

)
st.subheader(" Análise automática")

campanha_selecionada = st.selectbox(
    "Selecione uma campanha para analisar:",
    df["campanha"]
)

campanha = df[
    df["campanha"] == campanha_selecionada
].iloc[0]

st.markdown("### 📊 Métricas da campanha")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "CTR",
    f"{campanha['CTR']:.2f}%"
)

col2.metric(
    "CPC",
    f"R$ {campanha['CPC']:.2f}"
)

col3.metric(    
    "CPA",  
    f"R$ {campanha['CPA']:.2f}" 
)   

col4.metric(
    "ROAS",
    f"{campanha['ROAS']:.2f}x"
)

if st.button("Gerar análise"):
    resultado = analisar_campanha(campanha)

    st.success("Análise gerada com sucesso!")

    st.markdown("### Resultado da análise")
    st.write(resultado)