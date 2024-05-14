import streamlit as st
import numpy     as np
from f1 import f1
from c02_f01_get_config  import get_config
from sqlalchemy import create_engine, inspect
from c02_f02_get_tables  import get_tables
from c02_f03_get_db      import get_db


    

path_config = st.file_uploader("1.1 Path to config.csv file to access the DataBase:")

if not path_config:
  st.warning('To proceed upload the file "config.csv" first!')
  st.stop()

url = get_config(path_config)
st.write(url)

st.write("engine NOT created yet")
engine = create_engine(url)
st.write("engine created")

inspection   = inspect(engine)
table_names  = inspection.get_table_names("viuhydro_wx_data_v2")
table_names = [x for x in table_names if x.startswith("raw")]


db_path = st.selectbox( "1.2. Choose DataBase table to update (reload required if recently updated)", table_names, index = None )
if not db_path:
  st.warning('To proceed choose table to update first!')
  st.stop()
del table_names

# db_d, db_h, db_coltyp = get_db(url, db_path)

# with st.expander("Show the current DataBase table"):
    # st.dataframe(db_d)