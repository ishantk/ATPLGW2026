"""
    Streamlit
    Official Link: https://streamlit.io/
    pip install streamlit
"""

import streamlit as st
from Session13C import User
from Session13 import DBHelper

st.title('User Registration')
name = st.text_input('Enter Full Name')
phone = st.text_input('Enter Phone Number')
email = st.text_input('Enter Email')
password = st.text_input('Enter Password', type='password')

if st.button('Register'):

    user = User(name, phone, email, password)
    document_to_save = user.to_dictionary()

    db_helper = DBHelper()
    db_helper.select_collection()
    db_helper.save(document_to_save)

    # print('User Registered')
    # print(f'{name}, {phone}, {email}, {password}')