import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

conn = sqlite3.connect('carbon_credits.db')
df = pd.read_sql_query("SELECT * FROM bonos", conn)

st.title("🌍 Dashboard de Bonos de Carbono")
st.write("### Datos de Transacciones")
st.dataframe(df)