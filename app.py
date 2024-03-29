import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Fonction pour la page d'accueil
def home_page():
    st.title("Accueil")
    st.write("Bienvenue dans notre application de visualisation des données météorologiques!")

# Fonction pour une autre page, par exemple l'analyse des données
def data_analysis():
    st.title("Analyse des Données")
    st.write("Section d'analyse des données météorologiques.")


st.title("Visualisation des Données Météorologiques")



csv_file_path ='fev_24_to_mar_24.csv'
csv_file_path1 ='2010_2019.csv'
csv_file_path2 = 'avg_daily_temp_france.csv'
# Load your data
df = pd.read_csv(csv_file_path2, delimiter=';')

st.dataframe(df)





# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ('Accueil', 'Analyse des Données'))

if page == 'Accueil':
    home_page()
elif page == 'Analyse des Données':
    data_analysis()





