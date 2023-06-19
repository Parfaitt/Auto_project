import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Analyse exploratoire des données")

# Charger le fichier CSV
@st.cache
def charger_donnees(chemin_fichier):
    data = pd.read_csv(chemin_fichier)
    return data

# Interface utilisateur pour charger le fichier CSV
fichier_csv = st.file_uploader("Charger un fichier CSV", type=["csv"])

# Vérifier si un fichier a été chargé
if fichier_csv is not None:
    # Charger les données dans un DataFrame
    donnees = charger_donnees(fichier_csv)

    # Afficher les premières lignes des données
    st.subheader("Aperçu des données")
    st.write(donnees.head())

    # Afficher les statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(donnees.describe())

    # Afficher le nombre de lignes et de colonnes
    st.subheader("Dimensions des données")
    st.write("Nombre de lignes :", donnees.shape[0])
    st.write("Nombre de colonnes :", donnees.shape[1])

    # Afficher les noms des colonnes
    st.subheader("Colonnes des données")
    st.write(list(donnees.columns))

    # Afficher un graphique
    st.subheader("Graphique")
    # Exemple : histogramme d'une colonne
    colonne = st.selectbox("Sélectionnez une colonne pour l'histogramme", donnees.columns)
    st.bar_chart(donnees[colonne])

