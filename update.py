import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, get_customer, edit_customer_data


def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=[
                      'Customer Id', 'Customer Name', 'Doctor id', 'Phone Number', 'Address','Age'])
    with st.expander("Current Available customers"):
        st.dataframe(df)
    list_of_customer = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("Customer to Edit", list_of_customer)
    selected_result = get_customer(selected_customer)
    if selected_result:
        customerid = selected_result[0][0]
        customername = selected_result[0][1]
        doctorid = selected_result[0][2]
        phno = selected_result[0][3]
        addr = selected_result[0][4]
        age=selected_result[0][5]
        

        # Layout of Create

        new_customerid = st.text_input("Customer Id:", customerid)
        new_customername = st.text_input("Customer name:", customername)
        new_doctorid = st.text_input("Doctor Id:",doctorid)
        new_phno= st.text_input("Phone Number:", phno)
            
        new_addr = st.text_input("Address:", addr)
        new_age=st.text_input("Age",age)
        
        if st.button("Update"):
            edit_customer_data(new_customerid, new_customername, new_doctorid, new_phno,new_addr,new_age
                             ,customerid, customername, doctorid, phno, addr,age)
            st.success("Successfully updated:: {} to ::{} details".format(
                customername, new_customername))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=[
                       'Customer id', 'Customer name', 'Doctor id','Phone number', 'Address','Age'])
    with st.expander("Updated data"):
        st.dataframe(df2)