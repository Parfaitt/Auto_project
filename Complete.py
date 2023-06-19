import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    # Titre du projet
    st.title("Projet complet en data science")

    # Chargement du fichier CSV
    file = st.file_uploader("Charger un fichier CSV", type="csv")
    
    if file is not None:
        # Lecture des données CSV dans un dataframe
        df = pd.read_csv(file)
        
        # Affichage des données brutes
        st.subheader("Données brutes")
        st.write(df)
        
        # Nettoyage des données
        st.subheader("Nettoyage des données")
        
        # Suppression des valeurs manquantes
        st.write("Nombre de valeurs manquantes par colonne :")
        st.write(df.isnull().sum())
        
        # Traitement des valeurs manquantes
        df_cleaned = df.dropna()  # Suppression des lignes avec des valeurs manquantes
        
        # Affichage des données nettoyées
        st.subheader("Données nettoyées")
        st.write(df_cleaned)
        
        # Analyse exploratoire des données
        st.subheader("Analyse exploratoire des données")
        
        # Statistiques descriptives
        st.write("Statistiques descriptives :")
        st.write(df_cleaned.describe())
        
        # Visualisation des données
        
        # Histogramme interactif
        selected_column = st.selectbox("Sélectionnez une colonne pour l'histogramme", df_cleaned.columns)
        st.bar_chart(df_cleaned[selected_column])
        
        # Modélisation des données
        
        # Sélection de la colonne cible
        target_column = st.selectbox("Sélectionnez la colonne cible", df_cleaned.columns)
        
        # Séparation des données en features (X) et target (y)
        X = df_cleaned.drop(target_column, axis=1)
        y = df_cleaned[target_column]
        
        # Séparation des données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Choix du modèle de machine learning
        st.subheader("Choix du modèle de machine learning")
        models = {
            "Random Forest": RandomForestClassifier(),
            "Gradient Boosting": GradientBoostingClassifier(),
            "Logistic Regression": LogisticRegression()
        }
        selected_models = st.multiselect("Sélectionnez les modèles à entraîner", list(models.keys()))
        
        if selected_models:
            for model_name in selected_models:
                model = models[model_name]
                
                # Entraînement du modèle
                model.fit(X_train, y_train)
                
                # Prédictions sur l'ensemble de test
                y_pred = model.predict(X_test)
                
                # Évaluation de la performance
                accuracy = accuracy_score(y_test, y_pred)
                st.write(f"Précision du modèle {model_name} :", accuracy)
        
if __name__ == '__main__':
    main()
