import streamlit as st
import py_simple as ps
import requests
import time


ENDPOINT = "https://api.adviceslip.com/advice"
advice = requests.get(ENDPOINT).json()['slip']['advice']

col1, col2 = st.columns(2, gap="small", width=500)

with col1:
    st.title(advice)
with col2:
    st.image("smerf.jpg", width=400)