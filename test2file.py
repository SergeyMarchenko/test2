import streamlit as st
import numpy     as np
from f1 import f1
from c02_f01_get_config  import get_config
from sqlalchemy import create_engine, inspect


st.write("Coucou, here is a test app!")

b1 = st.button("Press", key = "b1")
if b1:
    mm = st.text_area('', "pressed!")
    if np.random.randint(0, 100)>50:
        st.balloons()
    else:
        st.snow()
   

b2 = st.button("Press", key = "b2")
if b2:
    message = f1()
    st.write(message)
    
    
st.write("1. DataBase table to join data to")
path_config = st.file_uploader("1.1 Path to config.csv file to access the DataBase:")

if not path_config:
  st.warning('To proceed upload the file "config.csv" first!')
  st.stop()

url = get_config(path_config)
st.write(url)