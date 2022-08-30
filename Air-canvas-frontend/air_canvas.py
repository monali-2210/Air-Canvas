import streamlit as st
import time
import pandas as pd

st.set_page_config(layout = "wide")

def Home():
    st.title("Project Air Canvas")

def ViewDemo():
    st.text("This is Demo page")
    #code for demo

def ViewCredits():
    st.text("This is credits page")
    #code for credits


with st.sidebar:
    page = st.sidebar.selectbox( 'DashBoard',['Home', 'View Demo', 'View Credits'])
    

if page == 'Home':
    Home()

elif page == 'View Demo':
    ViewDemo()

elif page == 'View Credits':
    ViewCredits()
