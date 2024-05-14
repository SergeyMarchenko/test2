import streamlit as st
import os
import numpy     as np
# from   sqlalchemy import create_engine
# from   sqlalchemy import inspect


# import plotly.graph_objects as go    
# import pandas               as pd


st.write("Welcome to the new app!")
x = np.arange(0, 11, 1)
st.write(x)


st.write(st.secrets["config_username"])

# conn = st.connection('mysql', type = 'sql')
# df = conn.query('SELECT * from raw_steph1_CSci_test;', ttl=600)
# st.write(df)
# st.dataframe(df)

# st.write("deleted code using functions from sqlalchemy")
# engine = create_engine(url)
# inspection   = inspect(engine)
# table_names  = inspection.get_table_names("viuhydro_wx_data_v2")
# table_names = [x for x in table_names if x.startswith("raw")]

# rng = np.random.default_rng()
# y = rng.integers(0, high=10, size=(1,10))

# import streamlit as st
# import os

# Everything is accessible via the st.secrets dict:
# st.write("DB username:", st.secrets["db_username"])
# st.write("DB password:", st.secrets["db_password"])
# st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:
# st.write(
    # "Has environment variables been set:",
    # os.environ["db_username"] == st.secrets["db_username"],
# )