import streamlit as st
import pandas as pd

def main():
    # Titre du tableau de bord
    st.title("Tableau de bord interactif des données")

    # Chargement du fichier CSV
    file = st.file_uploader("Charger un fichier CSV", type="csv")
    
    if file is not None:
        # Lecture des données CSV dans un dataframe
        df = pd.read_csv(file)
        
        # Affichage des données
        st.subheader("Données brutes")
        st.write(df)
        
        # Options de filtrage des données
        st.sidebar.subheader("Options de filtrage")
        column_to_filter = st.sidebar.selectbox("Choisissez une colonne pour filtrer", df.columns)
        filter_value = st.sidebar.text_input("Valeur à filtrer")
        
        # Filtrage des données
        filtered_df = df[df[column_to_filter] == filter_value]
        
        # Affichage des données filtrées
        st.subheader("Données filtrées")
        st.write(filtered_df)
        
        # Statistiques descriptives
        st.subheader("Statistiques descriptives")
        st.write(filtered_df.describe())

        # Visualisation des données
        st.subheader("Visualisation des données")
        
        # Histogramme interactif
        selected_column = st.selectbox("Sélectionnez une colonne pour l'histogramme", df.columns)
        st.bar_chart(df[selected_column])

        # Nuage de points interactif
        selected_columns = st.multiselect("Sélectionnez les colonnes pour le nuage de points", df.columns)
        if len(selected_columns) > 1:
            st.line_chart(df[selected_columns])

if __name__ == '__main__':
    main()
