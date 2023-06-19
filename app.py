import streamlit as st
import pandas as pd

def main():
    # Titre de l'application
    st.title("Analyse exploratoire des données")

    # Chargement du fichier CSV
    file = st.file_uploader("Charger un fichier CSV", type="csv")
    
    if file is not None:
        # Lecture des données CSV dans un dataframe
        df = pd.read_csv(file)
        
        # Affichage du dataframe
        st.subheader("Aperçu des données")
        st.write(df.head())

        # Informations sur les colonnes
        st.subheader("Informations sur les colonnes")
        st.write(df.info())

        # Statistiques descriptives
        st.subheader("Statistiques descriptives")
        st.write(df.describe())

        # Graphiques
        st.subheader("Visualisation des données")
        
        # Histogramme
        selected_column = st.selectbox("Sélectionnez une colonne", df.columns)
        st.bar_chart(df[selected_column])

        # Nuage de points
        selected_columns = st.multiselect("Sélectionnez les colonnes pour le nuage de points", df.columns)
        if len(selected_columns) > 1:
            st.line_chart(df[selected_columns])

if __name__ == '__main__':
    main()
