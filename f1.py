import numpy     as np
import streamlit as st
# message = f1()
@st.cache_data(show_spinner="Spinning...")
def f1():
    message = "this is a message generated by a function"
    
    if np.random.randint(0, 100)>50:
        st.balloons()
    else:
        st.snow()
   
    return message