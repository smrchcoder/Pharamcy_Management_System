import pandas as pd
import streamlit as st
from database import view_all_data, view_only_customer_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=[
                      'Customer Id ', 'Customer Name','Doctor Id', 'Phone Number', 'Address', 'Age'])
    with st.expander("Available Data"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("Task to Delete", list_of_customers)
    st.warning("Do you want to delete ::{}".format(selected_customer))
    if st.button("Delete Customer details"):
        delete_data(selected_customer)
        st.success("Customer details has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=[
                       'Customer ID', 'Customer Name',  'Doctor Id','Phone Number', 'Address','Age'])
    with st.expander("Updated data"):
        st.dataframe(df2)