import pickle
from pathlib import Path
import streamlit_authenticator as stauth

nomes = [
    'Diogo',
    'Gabriel',
    
]

usernames=[
     'Diogo',
     'gabriel',
]

senhas = ['2703','2707']

passwords = stauth.Hasher(senhas).generate()

file_path = Path(__file__).parent / 'hasher_pw.pkl'
with file_path.open('wb') as file:
    pickle.dump(passwords, file)
    