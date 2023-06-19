import streamlit as st
import openai

# Initialisation de l'API OpenAI
openai.api_key = 'YOUR_API_KEY'  # Remplacez YOUR_API_KEY par votre clé API OpenAI

def main():
    # Titre de l'application
    st.title("ChatGPT - Intelligence Artificielle")

    # Entrée de l'utilisateur
    user_input = st.text_input("Vous: ", "")

    if user_input:
        # Appel à l'API OpenAI pour obtenir une réponse
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50,
            temperature=0.7
        )

        # Sélection de la réponse générée
        reply = response.choices[0].text.strip()

        # Affichage de la réponse de l'IA
        st.text_area("IA: ", value=reply, height=200, max_chars=None)

if __name__ == '__main__':
    main()
