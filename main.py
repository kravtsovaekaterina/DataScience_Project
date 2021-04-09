import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame( {'x': [10, 20, 30, 40],
                    'y': [100, 200, 300, 400],
                    'name': ['alpha', 'beta', 'gamma', 'delta']})

x_max = st.slider('Max value of x', float(df['x'].max()))
st.title('My first app')
st.markdown("""
Let's look at this fine dataframe      
""")

df[df['x'] <= x_max]