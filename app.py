# Importing pakages
import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from query import run
import mysql.connector
def main():
    st.title("Pharmacy Mangement_425")
    menu = ["Add", "View", "update", "delete","run query"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "Add":
        st.subheader("Insert Customer Details:")
        create()

    elif choice == "View":
        st.subheader("View Created Customer Details")
        read()

    elif choice == "update":
        st.subheader("Update Inserted Details")
        update()

    elif choice == "delete":
        st.subheader("Delete Inserted Details")
        delete()
    elif choice=='run query':
        st.subheader("Run the query")
        run()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
