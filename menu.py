import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Titre de l'application
    st.title("Analyse des données avec Streamlit")

    # Chargement du fichier CSV
    file = st.file_uploader("Charger un fichier CSV", type="csv")

    if file is not None:
        # Lecture des données CSV dans un dataframe
        df = pd.read_csv(file)

        # Menu principal
        menu = ["Données brutes", "Visualisation"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Données brutes":
            # Affichage des données brutes
            st.subheader("Données brutes")
            st.write(df)

        elif choice == "Visualisation":
            # Analyse exploratoire des données
            st.subheader("Analyse exploratoire des données")

            # Résumé statistique
            st.write("Résumé statistique :")
            st.write(df.describe())

            # Histogramme des variables numériques
            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            selected_numeric_col = st.selectbox("Sélectionnez une variable numérique", numeric_cols)
            st.subheader(f"Histogramme de {selected_numeric_col}")
            plt.figure(figsize=(10, 6))
            sns.histplot(df[selected_numeric_col], kde=True)
            st.pyplot()

            # Diagramme en barres des variables catégorielles
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            selected_categorical_col = st.selectbox("Sélectionnez une variable catégorielle", categorical_cols)
            st.subheader(f"Diagramme en barres de {selected_categorical_col}")
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x=selected_categorical_col)
            plt.xticks(rotation=45)
            st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
    main()
