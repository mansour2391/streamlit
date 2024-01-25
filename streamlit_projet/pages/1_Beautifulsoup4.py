import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go  
import seaborn as sns
import matplotlib.pyplot as plt



Expat_ordi= pd.read_excel('EXPAT_ordi_bsoup4.xlsx')
Expat_telephone= pd.read_excel('EXPAT_telephone_bsoup4.xlsx')
Expat_tv= pd.read_excel('EXPAT_tv_bsoup4.xlsx')

def page1():
    
    st.markdown("<h1 style='color: red;'>Les données scrapées avec : Beautifulsoup4 </h1>", unsafe_allow_html=True)

    taches = ['1.Exploration des données dans notre documents','2. Exploration  de données dans le site', '2. Représentations graphiques(Dashbord)']
    choix =  ('Sélectionner une activité:', taches)
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

    elif choix == '2. Exploration  de données dans le site':

        affichages =['Afficher le dataset', 'Afficher les colonnes', 'Afficher Les variables', 'Le type des variables', 'Faire un summarise des données']
        affichage_select = st.sidebar.selectbox('Sélectionner un affichage:', affichages)

        if affichage_select == 'Afficher le dataset':
            st.write('# Base de données des Ordinateurs')
            st.write('----')
            st.success("Succès, veuillez retrouver votre base de données des ordinateurs, téléphones et TV de Expat Dakar.")
            st.info("Infos: Pour télécharger ce tableau, veuillez chercher l'icône de téléchargement en haut du tableau à droite.")
            st.info("Infos : Ces données ont été tres bien traitées.")
            slider = st.slider('Choisir l\'intervalle de valeurs à afficher', 1, Expat_ordi.shape[0], (500, 1500))
            st.dataframe(Expat_ordi.iloc[list(slider)[0]: list(slider)[1]])

            # Esthétique
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.write('----')
            st.write('# Base de données des Téléphones')
            st.write('----')
            slider = st.slider('Choisir l\'intervalle de valeurs à afficher', 1, Expat_telephone.shape[0], (500, 1000))
            st.dataframe(Expat_telephone.iloc[list(slider)[0]: list(slider)[1]])

            # Esthétique
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            
            st.write('----')
            st.write('# Base de données des TV')
            st.write('----')
            slider = st.slider('Choisir l\'intervalle de valeurs à afficher', 1, Expat_tv.shape[0], (200, 500))
            st.dataframe(Expat_tv.iloc[list(slider)[0]: list(slider)[1]])

        elif affichage_select == 'Afficher les colonnes':
            st.write('### Les colonnes de la base de donnee Ordinateur')
            column_select_ordi = st.sidebar.multiselect('Sélectionner une colonne pour les ordinateurs :', Expat_ordi.columns)
            if column_select_ordi:
                st.dataframe(Expat_ordi[column_select_ordi])
            else:
                st.error("Veuillez sélectionner au moins une colonne.")

            st.write('### Les colonnes de la base de donnee Téléphones')
            column_select_tel = st.sidebar.multiselect('Sélectionner une colonne pour les téléphones :', Expat_telephone.columns)
            if column_select_tel:
                st.dataframe(Expat_telephone[column_select_tel])
            else:
                st.error("Veuillez sélectionner au moins une colonne.")

            st.write('### Les colonnes de la base  de donnee Tv')
            column_select_tel = st.sidebar.multiselect('Sélectionner une colonne pour les tv :', Expat_tv.columns)
            if column_select_tel:
                st.dataframe(Expat_tv[column_select_tel])
            else:
                st.error("Veuillez sélectionner au moins une colonne.")


        elif affichage_select == 'Afficher Les variables':
            st.markdown("<h3>Prenons comme exemple le cas des Telephone</h3>", unsafe_allow_html=True)

            st.info('les variables sont les meme pour les differentes types de base de donnee , apart la dimension de l\'ecran qui s\'dans certains cas de figures')
            description_columns = dict()
            description_columns['details'] = "Ici il est question de dire de donnee les details du produits ds dans le cadre general  ..."
            description_columns['Etat'] = 'l\' etat ici determine si le produit est neuf,venant ou d\'ocassion..'
            description_columns['localite'] = "la localite ou le produit se trouve exactement"
            description_columns['region'] = "la Region ou se trouve la localite "
            description_columns['prix'] = "le prix du produit exprimer en FCFA"
            description_columns['image'] = "c' est le lien de l' image du produit"
            index = ['Description']
            description_columns_df = pd.DataFrame(description_columns, index=index)
            description_columns_df = description_columns_df.T
            # Affichage du DataFrame
            st.write(description_columns_df)

        elif affichage_select == 'Le type des variables':
    # Pour les ordinateurs
            dtype_columns_ordi = dict()
            for colonne in Expat_ordi.columns:
                dtype_columns_ordi[colonne] = Expat_ordi[colonne].dtype
            index_ordi = ['Dtype']
            dtypes_columns_df_ordi = pd.DataFrame(dtype_columns_ordi, index=index_ordi)
            dtypes_columns_df_ordi = dtypes_columns_df_ordi.T

    # Pour les téléphones
            dtype_columns_tel = dict()
            for colonne in Expat_telephone.columns:
                dtype_columns_tel[colonne] = Expat_telephone[colonne].dtype
            index_tel = ['Dtype']
            dtypes_columns_df_tel = pd.DataFrame(dtype_columns_tel, index=index_tel)
            dtypes_columns_df_tel = dtypes_columns_df_tel.T

    # Pour les tV
            dtype_columns_tv = dict()
            for colonne in Expat_tv.columns:
                dtype_columns_tv[colonne] = Expat_tv[colonne].dtype
            index_tel = ['Dtype']
            dtypes_columns_df_tv = pd.DataFrame(dtype_columns_tv, index=index_tel)
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
            st.info('INFO: ce describe se limite justement sur la variable prix')
            st.write('### Les ordinateurs')
            st.write(Expat_ordi.describe())
            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)
            st.write('### Les telephones')
            st.write(Expat_telephone.describe())
            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.write('### Les tv')
            st.write(Expat_tv.describe())


    
    elif choix == '2. Représentations graphiques(Dashbord)':
        plots = ['Répartition des états en fonction du prix de chaque base de données','Examiner comment la marque influence la perception du produit et son prix','Diagramme circulaire pour voir le taux de chaque Etat']
        plot_select = st.sidebar.selectbox('Sélectionner un plot:', plots)
        st.subheader(plot_select)

        if plot_select == 'Répartition des états en fonction du prix de chaque base de données':
        # Créer un graphique en barres dynamique avec heatmap pour Expat_ordi
            fig_ordi = px.histogram(Expat_ordi, x="etat", color="prix", barmode="group", title="Répartition des états de l'ordinateur en fonction du prix")

        # Ajouter une coloration heatmap
            fig_ordi.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGray')),
                               selector=dict(type='bar'))

            # Afficher le graphique
            st.plotly_chart(fig_ordi)

            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            # Créer un graphique en barres dynamique avec heatmap pour Expat_telephone
            fig_telephone = px.histogram(Expat_telephone, x="etat", color="prix", barmode="group", title="Répartition des états des téléphones en fonction du prix")

            # Ajouter une coloration heatmap
            fig_telephone.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGray')),
                                        selector=dict(type='bar'))

            # Afficher le graphique
            st.plotly_chart(fig_telephone)

            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            # Créer un graphique en barres dynamique avec heatmap pour Expat_tv
            fig_tv = px.histogram(Expat_tv, x="etat", color="prix", barmode="group", title="Répartition des états des TV en fonction du prix")

            # Ajouter une coloration heatmap
            fig_tv.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGray')),
                                selector=dict(type='bar'))

            # Afficher le graphique
            st.plotly_chart(fig_tv)
        
        elif plot_select == 'Examiner comment la marque influence la perception du produit et son prix':
            st.markdown('<h3>Influence de la marque des ordinateurs sur la perception et le prix </h3>', unsafe_allow_html=True)


            # Sélectionne les colonnes pertinentes 
            cols_selectionnees = ['marque', 'prix']
            df_selectionne = Expat_ordi[cols_selectionnees]

            # Utilise Seaborn pour créer un bar plot de la moyenne du prix pour chaque marque
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.barplot(x='marque', y='prix', data=df_selectionne, ci=None, ax=ax)  # ci=None pour ne pas afficher l'intervalle de confiance
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotation des étiquettes pour une meilleure lisibilité
            st.pyplot(fig)

            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.markdown('<h3>Influence de la marque des telephones sur la perception et le prix </h3>', unsafe_allow_html=True)


            # Sélectionne les colonnes pertinentes 
            cols_selectionnees1 = ['marque', 'prix']
            df_selectionne1 = Expat_telephone[cols_selectionnees1]

            # Utilise Seaborn pour créer un bar plot de la moyenne du prix pour chaque marque
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.barplot(x='marque', y='prix', data=df_selectionne1, ci=None, ax=ax)  # ci=None pour ne pas afficher l'intervalle de confiance
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotation des étiquettes pour une meilleure lisibilité
            st.pyplot(fig)

            # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)

            st.markdown('<h3>Influence de la marque des tv sur la perception et le prix </h3>', unsafe_allow_html=True)


            # Sélectionne les colonnes pertinentes 
            cols_selectionnees2 = ['marque', 'prix']
            df_selectionne2 = Expat_tv[cols_selectionnees2]

            # Utilise Seaborn pour créer un bar plot de la moyenne du prix pour chaque marque
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.barplot(x='marque', y='prix', data=df_selectionne2, ci=None, ax=ax)  # ci=None pour ne pas afficher l'intervalle de confiance
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotation des étiquettes pour une meilleure lisibilité
            st.pyplot(fig)

        elif plot_select == 'Diagramme circulaire pour voir le taux de chaque Etat':
            # Exemple de données du dataframe Expat_ordi (remplace-le par ton vrai dataframe)
            df_select_ordi = Expat_ordi['etat']

            # Sélection des données pour le camembert
            data_etat_ordi = df_select_ordi.value_counts()

            # Création du camembert avec Plotly
            fig_etat_ordi = go.Figure(data=[go.Pie(labels=data_etat_ordi.index, values=data_etat_ordi, hole=0.4)])
            fig_etat_ordi.update_layout(title_text='Diagramme circulaire pour voir le taux de chaque Etat ordinateur ')

            # Afficher le camembert
            st.plotly_chart(fig_etat_ordi)

                        # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)


                            # Exemple de données du dataframe Expat_ordi (remplace-le par ton vrai dataframe)
            df_select_telephone = Expat_telephone['etat']

            # Sélection des données pour le camembert
            data_etat_telephone = df_select_telephone.value_counts()

            # Création du camembert avec Plotly
            fig_etat_telephone = go.Figure(data=[go.Pie(labels=data_etat_ordi.index, values=data_etat_telephone, hole=0.4)])
            fig_etat_telephone.update_layout(title_text='Diagramme circulaire pour voir le taux de chaque Etat telephone')

            # Afficher le camembert
            st.plotly_chart(fig_etat_telephone)


                        # Barre de progression
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)


                            # Exemple de données du dataframe Expat_ordi (remplace-le par ton vrai dataframe)
            df_select_tv= Expat_tv['etat']

            # Sélection des données pour le camembert
            data_etat_tv = df_select_tv.value_counts()

            # Création du camembert avec Plotly
            fig_etat_tv = go.Figure(data=[go.Pie(labels=data_etat_ordi.index, values=data_etat_tv, hole=0.4)])
            fig_etat_tv.update_layout(title_text='Diagramme circulaire pour voir le taux de chaque Etat tv')

            # Afficher le camembert
            st.plotly_chart(fig_etat_tv)

            
page1()