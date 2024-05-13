import streamlit as st
import numpy     as np
from f1 import f1
from c02_f01_get_config  import get_config
from sqlalchemy import create_engine, inspect
from c02_f02_get_tables  import get_tables
from c02_f03_get_db      import get_db


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

table_names = get_tables(url)
db_path = st.selectbox( "1.2. Choose DataBase table to update (reload required if recently updated)", table_names, index = None )
#
# db_path = 'raw_steph1_CSci_test_upd_20240430'
#
if not db_path:
  st.warning('To proceed choose table to update first!')
  st.stop()
del table_names

db_d, db_h, db_coltyp = get_db(url, db_path)

with st.expander("Show the current DataBase table"):
    st.dataframe(db_d)