import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Titre de l'application
st.title('Analyse de la Température en France')

# Description de l'application
st.write("""
Cette application présente une analyse approfondie des données de température en France. En utilisant des techniques de décomposition saisonnière, 
nous explorons les composants sous-jacents des séries temporelles des températures, incluant la tendance, la saisonnalité, et les résidus. 
Cela permet de mieux comprendre les variations de température au fil du temps et d'identifier des modèles ou des anomalies potentielles.
""")

# Fonction pour charger et préparer les données
def load_data():
    df = pd.read_csv('temp_france.csv', sep=';', decimal=',')
    df['DATE'] = pd.to_datetime(df['DATE'])
    if df['T_Q_Moyenne'].dtype == 'O':
        df['T_Q_Moyenne'] = df['T_Q_Moyenne'].str.replace(',', '.').astype(float)
    return df

# Chargement et préparation des données
df = load_data()

df = df.sort_values('DATE')

# Calcul de la décomposition saisonnière
# Notez que la période doit être adaptée en fonction de la fréquence et de la granularité de vos données
additive_decomposition = seasonal_decompose(df['T_Q_Moyenne'], model='additive', period=365)

# Préparation de la figure pour la décomposition
fig, ax = plt.subplots(4, 1, figsize=(10, 8))

additive_decomposition.observed.plot(ax=ax[0], legend=False)
ax[0].set_ylabel('Observé')

additive_decomposition.trend.plot(ax=ax[1], legend=False)
ax[1].set_ylabel('Tendance')

additive_decomposition.seasonal.plot(ax=ax[2], legend=False)
ax[2].set_ylabel('Saisonnalité')

additive_decomposition.resid.plot(ax=ax[3], legend=False)
ax[3].set_ylabel('Résidu')

plt.tight_layout()

# Affichage de la figure dans Streamlit
st.pyplot(fig)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# Fonction pour charger et préparer les données
def load_data():
    # Assurez-vous que le chemin vers le fichier CSV est correct et accessible
    df = pd.read_csv('temp_france.csv', sep=';', decimal=',')
    df['DATE'] = pd.to_datetime(df['DATE'])
    # Vérifie si 'T_Q_Moyenne' est de type object (chaîne), puis remplace ',' par '.' et convertit en float
    if df['T_Q_Moyenne'].dtype == 'O':  # 'O' pour object, indiquant une chaîne ou un mix de types
        df['T_Q_Moyenne'] = df['T_Q_Moyenne'].str.replace(',', '.').astype(float)
    return df

# Chargement et préparation des données
df = load_data()

# Création de l'interface utilisateur Streamlit
st.title('Dashboard Météorologique de la France')


# Sélecteur de date
start_date, end_date = st.select_slider(
    'Sélectionnez la plage de date:',
    options=pd.to_datetime(df['DATE']).dt.date.unique(),
    value=(pd.to_datetime(df['DATE']).dt.date.min(), pd.to_datetime(df['DATE']).dt.date.max())
)

# Filtrage des données basé sur la sélection de date
filtered_df = df[(df['DATE'].dt.date >= start_date) & (df['DATE'].dt.date <= end_date)]

# Affichage des données filtrées et visualisation
st.write(f'Visualisation des températures moyennes du {start_date} au {end_date}')
fig = px.line(filtered_df, x='DATE', y='T_Q_Moyenne', title='Température Moyenne au fil du Temps', labels={'T_Q_Moyenne': 'Température Moyenne (°C)'})
st.plotly_chart(fig)






