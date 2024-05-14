import streamlit as st
import numpy     as np
from   sqlalchemy import create_engine
# from   sqlalchemy import inspect


# import plotly.graph_objects as go    
# import pandas               as pd


st.write("Welcome to the new app!")
x = np.arange(0, 11, 1)
st.write(x)

url = "mysql+mysqlconnector://viuhydro_shiny:.rt_BKD_SB*Q@192.99.62.147:3306/viuhydro_wx_data_v2"
st.write(url)

st.write("added import of functions from sqlalchemy")
st.write("added code using functions from sqlalchemy")
engine = create_engine(url)
# inspection   = inspect(engine)
# table_names  = inspection.get_table_names("viuhydro_wx_data_v2")
# table_names = [x for x in table_names if x.startswith("raw")]

# rng = np.random.default_rng()
# y = rng.integers(0, high=10, size=(1,10))

