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

    st.success('User Registered Successfully')

    # print('User Registered')
    # print(f'{name}, {phone}, {email}, {password}')

# Explore how to create a Form in Streamlit
# Streamlit success error messages to be printed
# Check for fields i.e. validation eg password lenght > 6 or email cannot be empty
# After the succesfull db insertion, navigate to a new Page stating welcome to home