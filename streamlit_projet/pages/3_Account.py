import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('projet-data-collection-6d347e9585ac.json')

# Vérifier si l'application Firebase est déjà initialisée
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome')
    choix = st.selectbox('Login/Signup', ['login', 'Sign Up'])


        
    def f():
        try:
            user = auth.get_user_by_email(email)
            st.success('Connection réussie')
            #print(user.uid)

        except:
            st.warning('Connection échouée')

    if choix == 'login':
        email = st.text_input('Email Adresse')
        password = st.text_input("Password", type="password")
        st.button('Login', on_click=f)

    else:
        email = st.text_input('Email Adresse')
        password = st.text_input("Password", type="password")
        username = st.text_input('Entrer votre nom d utilisateur')

        if st.button('Créer mon compte'):
            user = auth.create_user(email=email, password=password, uid=username)
            st.success('Compte créé avec succès')
            st.markdown('Veuillez vous connecter avec votre email et mot de passe')
            st.balloons()

app()
