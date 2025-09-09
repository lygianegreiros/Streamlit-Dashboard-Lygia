import requests
import pandas as pd
import streamlit as st
import plotly.express as px

URL = "https://api.thingspeak.com/channels/2943258/feeds.json"

@st.cache_data
def load_data():
    response = requests.get(URL)
    data = response.json()
    feeds = data["feeds"]
    df = pd.DataFrame(feeds)
    df["created_at"] = pd.to_datetime(df["created_at"])
    df = df.rename(columns={
        "field1": "Umidade",
        "field2": "Temperatura"
    })
    
    df["Umidade"] = pd.to_numeric(df["Umidade"], errors="coerce")
    df["Temperatura"] = pd.to_numeric(df["Temperatura"], errors="coerce")

    return df[["created_at", "Umidade", "Temperatura"]]

# Aplicativo
st.title("🌾 Dashboard - Umidade & Temperatura")
df = load_data()
st.write("📋 Prévia dos dados:", df.head())

# Abas de umidade e temperatura
tab1, tab2 = st.tabs(["💧 Umidade", "🌡️ Temperatura"])

# Aba de Umidade
with tab1:
    st.subheader("📈 Evolução da Umidade")
    st.line_chart(df.set_index("created_at")["Umidade"])

    st.subheader("📊 Distribuição (Barras)")
    fig_bar = px.histogram(df, x="Umidade", nbins=10, title="Distribuição da Umidade")
    st.plotly_chart(fig_bar)

    st.subheader("🥧 Proporção por faixas")
    bins = pd.cut(df["Umidade"].dropna(), bins=5)
    pie_data = bins.value_counts().reset_index()
    pie_data.columns = ["Faixa", "Contagem"]
    pie_data["Faixa"] = pie_data["Faixa"].astype(str)
    fig_pie = px.pie(pie_data, values="Contagem", names="Faixa", title="Proporção da Umidade")
    st.plotly_chart(fig_pie)

    st.metric("Última Umidade (%)", f"{df['Umidade'].dropna().iloc[-1]:.1f}")

# Aba de Temperatura 
with tab2:
    st.subheader("📈 Evolução da Temperatura")
    st.line_chart(df.set_index("created_at")["Temperatura"])

    st.subheader("📊 Distribuição (Barras)")
    fig_bar = px.histogram(df, x="Temperatura", nbins=10, title="Distribuição da Temperatura")
    st.plotly_chart(fig_bar)

    st.subheader("🥧 Proporção por faixas")
    bins = pd.cut(df["Temperatura"].dropna(), bins=5)
    pie_data = bins.value_counts().reset_index()
    pie_data.columns = ["Faixa", "Contagem"]
    pie_data["Faixa"] = pie_data["Faixa"].astype(str)
    fig_pie = px.pie(pie_data, values="Contagem", names="Faixa", title="Proporção da Temperatura")
    st.plotly_chart(fig_pie)

    st.metric("Última Temperatura (°C)", f"{df['Temperatura'].dropna().iloc[-1]:.1f}")
