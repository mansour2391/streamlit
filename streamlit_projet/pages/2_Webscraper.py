import streamlit as st
import pandas as pd

expat_webscrap_ordi = pd.read_excel('ordi_expat.xlsx')
expat_webscrap_telephone = pd.read_excel('telephone_expat.xlsx')
expat_webscrap_tv = pd.read_excel('tv_expat.xlsx')

def page2():
    #st.title(" Les données scrapées avec : <font color='blue'>Web Scraper</font>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: blue;'>Les données scrapées avec : Web Scraper</h1>", unsafe_allow_html=True)

    taches = ['1.Exploration des données dans notre documents','2. Exploration de données dans le site ']
    choix = st.sidebar.selectbox('Sélectionner une activité:', taches)
    st.subheader(choix)

    if choix == '1.Exploration des données dans notre documents':
        

        st.write("### Lecture de fichiers xlsx avec Streamlit")


    # Affichez un widget pour uploader des fichiers CSV
        televerser_fichier = st.file_uploader("Choisissez un fichier XLSX", type=["xlsx"])

        if televerser_fichier is not None:
        # Lisez le fichier CSV
            df = pd.read_excel(televerser_fichier)
        # Affichez les données
            st.write("Contenu du fichier xlsx :")
            st.dataframe(df)

    elif choix == '2. Exploration de données dans le site ':
        affichages =['Afficher le dataset', 'Afficher les colonnes', 'Afficher Les variables', 'Le type des variables', 'Faire un summarise des données']
        affichage_select = st.sidebar.selectbox('Sélectionner un affichage:', affichages)

        if affichage_select == 'Afficher le dataset':
            st.write('### Base de données des Ordinateurs')
            st.write('----')
            st.success("Succès, veuillez retrouver votre base de données des ordinateurs, téléphones et TV de Expat Dakar.")
            st.info("Infos: Pour télécharger ce tableau, veuillez chercher l'icône de téléchargement en haut du tableau à droite.")
            st.warning("Attention : Ces données n'ont pas été traitées.")
            slider = st.slider('Choisir l\'intervalle de valeurs à afficher', 1, expat_webscrap_ordi.shape[0], (200, 500))
            st.dataframe(expat_webscrap_ordi.iloc[list(slider)[0]: list(slider)[1]])

            # Esthétique
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.write('----')
            st.write('### Base de données des Téléphones')
            st.write('----')
            slider = st.slider('Choisir l\'intervalle de valeurs à afficher', 1, expat_webscrap_telephone.shape[0], (200, 500))
            st.dataframe(expat_webscrap_telephone.iloc[list(slider)[0]: list(slider)[1]])

            # Esthétique
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.write('----')
            st.write('### Base de données des Tv')
            st.write('----')
            slider = st.slider('Choisir l\'intervalle de valeurs à afficher', 1, expat_webscrap_tv.shape[0], (200, 500))
            st.dataframe(expat_webscrap_tv.iloc[list(slider)[0]: list(slider)[1]])


        elif affichage_select == 'Afficher les colonnes':
            st.write('### Les colonnes de la base Ordinateur')
            column_select_ordi = st.sidebar.multiselect('Sélectionner une colonne pour les ordinateurs :', expat_webscrap_ordi.columns)
            if column_select_ordi:
                st.dataframe(expat_webscrap_ordi[column_select_ordi])
            else:
                st.error("Veuillez sélectionner au moins une colonne.")

            st.write('### Les colonnes de la base Téléphones')
            column_select_tel = st.sidebar.multiselect('Sélectionner une colonne pour les téléphones :', expat_webscrap_telephone.columns)
            if column_select_tel:
                st.dataframe(expat_webscrap_telephone[column_select_tel])
            else:
                st.error("Veuillez sélectionner au moins une colonne.")

                st.write('### Les colonnes de la base Tv')
            column_select_tv = st.sidebar.multiselect('Sélectionner une colonne pour les tv :', expat_webscrap_tv.columns)
            if column_select_tv:
                st.dataframe(expat_webscrap_tv[column_select_tv])
            else:
                st.error("Veuillez sélectionner au moins une colonne.")





        ##Shapes of dataset
        elif affichage_select == 'Afficher Les variables':
            st.markdown("<h3>Prenons comme exemple le cas des ordinateurs</h3>", unsafe_allow_html=True)

            st.info('les variables sont les meme pour les differentes types de base de donnee , apart la dimension de l\'ecran qui s\'dans certains cas de figures')
            description_columns = dict()
            description_columns['Etatordi'] = "Ici il est question de dire si les produits sont de types venant ou occasions ..."
            description_columns['marque'] = " La marque du produit "
            description_columns['couleur'] = "Couleur du produit"
            description_columns['processeur'] = "Les caracteristiques du processeur"
            description_columns['ram'] = "les capacites de la RAM(random acess memory)"
            description_columns['stockage'] = "Le stockage du produit en terme de giga"
            description_columns['prix'] = "le prix du produit exprimer en FCFA"
            index = ['Description']
            description_columns_df = pd.DataFrame(description_columns, index=index)
            description_columns_df = description_columns_df.T
            # Affichage du DataFrame
            st.write(description_columns_df)

        elif affichage_select == 'Le type des variables':
    # Pour les ordinateurs
            dtype_columns_ordi = dict()
            for colonne in expat_webscrap_ordi.columns:
                dtype_columns_ordi[colonne] = expat_webscrap_ordi[colonne].dtype
            index_ordi = ['Dtype']
            dtypes_columns_df_ordi = pd.DataFrame(dtype_columns_ordi, index=index_ordi)
            dtypes_columns_df_ordi = dtypes_columns_df_ordi.T

    # Pour les téléphones
            dtype_columns_tel = dict()
            for colonne in expat_webscrap_telephone.columns:
                dtype_columns_tel[colonne] = expat_webscrap_telephone[colonne].dtype
            index_tel = ['Dtype']
            dtypes_columns_df_tel = pd.DataFrame(dtype_columns_tel, index=index_tel)
            dtypes_columns_df_tel = dtypes_columns_df_tel.T

            dtypes_columns_df_tv = dict()
            for colonne in expat_webscrap_tv.columns:
                dtypes_columns_df_tv[colonne] = expat_webscrap_tv[colonne].dtype
            index_tv = ['Dtype']
            dtypes_columns_df_tv = pd.DataFrame(dtypes_columns_df_tv, index=index_tv)
            dtypes_columns_df_tv = dtypes_columns_df_tv.T


    # Affichage des DataFrames
            st.write('### Le type des variables pour les ordinateurs')
            st.write(dtypes_columns_df_ordi)
       
            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.write('### Le type des variables pour les téléphones')
            st.write(dtypes_columns_df_tel)

            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.write('### Le type des variables pour les tv')
            st.write(dtypes_columns_df_tv)



        elif affichage_select == 'Faire un summarise des données':
            st.write(expat_webscrap_ordi.describe())
             
            st.write(expat_webscrap_telephone.describe())
            st.write(expat_webscrap_tv.describe())
            st.write("""
- count: Nombre total d'observations non manquantes.
- unique: Nombre d'éléments uniques.
- top: La valeur la plus fréquente.
- freq: La fréquence de la valeur la plus fréquente (top).
""")

# Afficher la page sélectionnée
page2()

