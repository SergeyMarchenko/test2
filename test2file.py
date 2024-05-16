import streamlit as st
import numpy     as np




st.write("Welcome to the new app!")

b = st.button("Press the button!", key = "b1")
if b:
    mm = st.text_area('', "pressed!")
    
    if np.random.randint(0, 100)>50:
        st.balloons()
    else:
        st.snow()
