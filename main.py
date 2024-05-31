# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1owi3NmIRrwTuhIdctReImQLg-NwtUUtv
"""

import streamlit as st
from web_function import load _data

from Tabs import homr,predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

#membuat sidebar
st.sidebar.tittle("Navigasi")

#memnuat radio option
page = st.sidebar.radio("Pages",list(Tabs.keys()))

#load dataset
df, x,y =load_data()

#kondisi call app function
if page in ["Prediction","Visualisation"]:
  Tabs[page].app(df, x,y)
else:
  Tabs[page].app()