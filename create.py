import streamlit as st
from database import add_data


def create():
        customerid = st.text_input("Customer Id:")
        customername = st.text_input("Customer Name:")
        doctorid = st.text_input("Doctor id :")
        phno= st.text_input("Phone Number:")
        addr = st.text_input("Address:")
        age=st.text_input("Age")
        
        
        if st.button("Add Customer"):
            add_data(customerid, customername, doctorid, phno,addr,age)
            st.success("Successfully added Customer: {}".format(customername))