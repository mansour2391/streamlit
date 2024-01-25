

from streamlit.components.v1 import declare_component
import streamlit as st
import pandas as pd

# Page d'accueil
if page == "Accueil":
    st.title("Bienvenue sur la page d'accueil")
    st.write("Sélectionnez une page à partir de la barre latérale.")


# Créer un DataFrame de test
data = {'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
        'Âge': [25, 30, 35, 40],
        'Ville': ['Paris', 'New York', 'London', 'Berlin']}

df = pd.DataFrame(data)

# Titre de l'application
st.title("Ma Première Application Streamlit")

# Afficher le DataFrame
st.write("Voici un DataFrame de test :")
st.dataframe(df)

# Bouton pour afficher les statistiques
if st.button("Afficher les statistiques"):
    st.write("Statistiques du DataFrame :")
    st.write(df.describe())

# Bouton pour afficher les noms
if st.button("Afficher les noms"):
    st.write("Noms dans le DataFrame :")
    st.write(df['Nom'])

    # Sélecteur de colonnes
    selected_column = st.selectbox("Sélectionnez une colonne :", df.columns)
    st.write(f"Vous avez sélectionné la colonne : {selected_column}")

    # Barre de progression
    st.write('votre barre')
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    # Affichage d'une image
    st.image("https://placekitten.com/500/300", caption="Image de chaton", use_column_width=True)

    # Ajout de texte
    st.markdown("C'est une application simple créée avec Streamlit.")


    # Déclarer le composant pour la navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Aller à :", ["Accueil", "Page 1", "Page 2"])

    # Définir le composant de navigation
    st.set_page_config(page_title="Application Multi-pages", page_icon=":smiley:")


# Page 1
elif page == "Page 1":
    st.title("Page 1")
    st.write("Contenu de la page 1.")

# Page 2
elif page == "Page 2":
    st.title("Page 2")
    st.write("Contenu de la page 2.")

