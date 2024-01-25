
import streamlit as st 
from PIL import Image
import pandas as pd

from firebase_admin import credentials
from firebase_admin import auth


def main():


    st.header('')

    st.sidebar.write("----")
    st.sidebar.title('GROUPE 1 : MANSOUR SOW - ALIOU BA ')
    st.sidebar.write("----")

    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
    st.title('Projet Scraping avec  Streamlit en Licence 2_DIT 👋 ')
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
        

if __name__=='__main__':
    main()


def main():
    
              

              

    st.title(" BeautifulSoup4 - Web Scraper")

    # Image pour une illustration visuelle
    image = Image.open("scrapin.png")
    st.image(image, caption="Illustration du Web Scraping", use_column_width=True)

    st.write(
        """
        Le web scraping est une technique permettant d'extraire des informations utiles à partir de pages web. Il est souvent utilisé pour collecter des données à des fins d'analyse, de recherche ou d'automatisation de tâches.

        ## BeautifulSoup4

        BeautifulSoup4 est une bibliothèque Python qui facilite l'extraction des données à partir de fichiers HTML et XML. Elle offre une syntaxe Pythonic élégante pour naviguer et rechercher des éléments dans le code source d'une page web. En utilisant BeautifulSoup4, les développeurs peuvent extraire des informations spécifiques en fonction des balises HTML et de leur structure.

        ## Web Scraper

        Web Scraper, d'autre part, est un outil plus général qui peut désigner toute méthode automatisée pour extraire des données à partir du web. Cela peut inclure l'utilisation de bibliothèques comme BeautifulSoup4, mais également d'autres méthodes plus avancées, telles que l'utilisation d'APIs ou de frameworks de scraping.

        ## Similitudes

        Les deux approches partagent l'objectif d'extraire des informations depuis le web, mais elles diffèrent dans la manière dont elles atteignent cet objectif.

        ## Différences

        BeautifulSoup4 est spécifiquement conçu pour analyser la structure HTML ou XML d'une page web et extraire des données en fonction de cette structure. En revanche, un web scraper peut impliquer différentes techniques, y compris l'automatisation de l'interaction avec les pages web via un navigateur.

        Dans cette application Streamlit, vous pouvez explorer les données extraites avec ces deux approches en sélectionnant les différentes options dans la barre latérale.

        """
    )

if __name__ == "__main__":
    main()

st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            right: 0;
            width: 100%;
            text-align: right;
            padding: 10px;
            background-color: #000000;
            color: white;
        }
    </style>
    <div class="footer">
        <p>Source Google / Page d'Accueil / Groupe 1 </p>
    </div>
    """,
    unsafe_allow_html=True
)

