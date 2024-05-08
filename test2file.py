import streamlit as st
from f1 import f1

st.write("Coucou, here is a test app!")

b1 = st.button("Press", key = "b1")
if b1:
    mm = st.text_area('', "pressed!")
    st.balloons()
   

b2 = st.button("Press", key = "b2")
if b2:
    message = f1()
    st.write(message)