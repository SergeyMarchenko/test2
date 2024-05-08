import numpy     as np
import streamlit as st

st.write("Coucou")
b = st.button("Press", key = "b")
if b:
    mm = st.text_area('', "pressed!")
    
    if np.random.randint(0, 100)>50:
        st.balloons()
    else:
        st.snow()

st.write('look, there is a new line in the code!')

st.write('a second additional line of code')