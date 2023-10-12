import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data,view1


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=[
                      'Customer Id', 'Customer Name','Doctor ID' ,'Phone Number', 'Address' ,'Age'])
    with st.expander("View Customer Details"):
        st.dataframe(df)
    df1=view1()
    df1=pd.DataFrame(df1,columns=['drug name','stock required'])
    
    with st.expander("Graph"):
        '''
        task_df = df1['drug name'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)'''
        st.dataframe(df1)
        p1 = px.pie(df1, names='drug name', values='stock required') 
        st.plotly_chart(p1)
