import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a page header
st.header("Welcome to Titanic Analysis Homepage 👋")


# Create three columns
col1, col2 = st.columns([1,1])


with col1:
    img = Image.open('images/titanic-dicaprio-winslet.jpg')
    st.image(img)
    # display the link to that page.
    st.write('<a href="/exploratory_data_analysis.py"> Exploratory Data Analysis</a>', unsafe_allow_html=True)

with col2:
    img = Image.open('images/Logitstic+regression+formula.jpg')
    st.image(img)
    # display the link to that page.
    st.write('<a href="/titanic_model.py"> Exploratory Data Analysis</a>', unsafe_allow_html=True)