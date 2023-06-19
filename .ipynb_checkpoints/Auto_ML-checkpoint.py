import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, confusion_matrix, classification_report

def main():
    # Titre du projet
    st.title("Projet de Data Science avec Streamlit")

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
        
        # Sélection de la colonne cible
        target_column = st.selectbox("Sélectionnez la colonne cible", df_cleaned.columns)
        
        # Séparation des données en features (X) et target (y)
        X = df_cleaned.drop(target_column, axis=1)
        y = df_cleaned[target_column]
        
        # Séparation des données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Entraînement des modèles de régression
        st.subheader("Entraînement des modèles de régression")
        
        models_regression = {
            "Random Forest Regression": RandomForestRegressor(),
            "Gradient Boosting Regression": GradientBoostingRegressor()
        }
        
        for model_name, model in models_regression.items():
            # Entraînement du modèle
            model.fit(X_train, y_train)
            
            # Prédictions sur l'ensemble de test
            y_pred = model.predict(X_test)
            
            # Évaluation du modèle
            st.subheader(f"Modèle de régression : {model_name}")
            r2 = r2_score(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            
            st.write(f"R2 Score : {r2}")
            st.write(f"MSE : {mse}")
        
        # Entraînement des modèles de classification
        st.subheader("Entraînement des modèles de classification")
        
        models_classification = {
            "Random Forest Classification": RandomForestClassifier(),
            "Gradient Boosting Classification": GradientBoostingClassifier()
        }
        
        for model_name, model in models_classification.items():
            # Entraînement du modèle
            model.fit(X_train, y_train)
            
            # Prédictions sur l'ensemble de test
            y_pred = model.predict(X_test)
            
            # Évaluation du modèle
            st.subheader(f"Modèle de classification : {model_name}")
            accuracy = accuracy_score(y_test, y_pred)
            cm = confusion_matrix(y_test, y_pred)
            classification_rep = classification_report(y_test, y_pred)
            
            st.write(f"Accuracy : {accuracy}")
            st.write("Matrice de confusion :")
            st.write(cm)
            st.write("Rapport de classification :")
            st.write(classification_rep)
            
if __name__ == '__main__':
    main()
