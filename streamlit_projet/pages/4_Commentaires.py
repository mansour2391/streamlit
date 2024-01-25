import streamlit as st
import pandas as pd

def create_user_profile():
    # Titre de l'application
    st.title("Formulaire + commentaires")

    # Saisie des informations utilisateur
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    
    # Niveau d'études
    niveau_etude_options = ['Étudiant', 'Docteur', 'Ingénieur']
    niveau_etude = st.selectbox("Niveau d'études", niveau_etude_options)

    adresse = st.text_input("Adresse")

    # Vérification des informations obligatoires
    if not nom or not prenom or not niveau_etude or not adresse:
        st.warning("Veuillez remplir tous les champs obligatoires.")
        return

    commentaire = st.text_area("Commentaire")

    # Bouton d'envoi
    if st.button("Envoyer"):
        # Notification de succès
        st.success("Données envoyées avec succès! 🎉")

        # Création d'un DataFrame avec les données
        data = {'Nom': [nom], 'Prénom': [prenom], 'Niveau d\'études': [niveau_etude], 'Adresse': [adresse], 'Commentaire': [commentaire]}
        df = pd.DataFrame(data)

        # Enregistrement des données dans un fichier CSV
        df.to_csv('user_data.csv', index=False)

        # Affichage des données saisies
        st.subheader("Données saisies:")
        st.write(df)

        # Balloons pour célébrer
        st.balloons()

# Exécution de la fonction pour créer le formulaire
create_user_profile()
