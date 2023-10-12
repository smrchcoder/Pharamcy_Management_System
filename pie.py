import pandas as pd
import streamlit as st
from database1 import view1
import plotly.express as px
import numpy as np


def view():
    result = view1()
    df = pd.DataFrame(result, columns=[
                      'Name', 'Customers'])
    with st.expander("View Customers"):
        st.dataframe(df)
    with st.expander("Bar Plot of Customers"):
        st.bar_chart(data=df, x='Name', y='Customers')

    with st.expander("Pie Plot of Customers"):
        p1 = px.pie(df, names='Name', values='Customers')
        st.plotly_chart(p1)