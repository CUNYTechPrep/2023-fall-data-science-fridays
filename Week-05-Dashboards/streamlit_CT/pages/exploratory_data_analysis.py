import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt


st.title("Visualization of Titanic Data")


img = Image.open("images/titanic.jpeg")
st.image(img, width=600, caption="Image of Titanic Ship")


# txt= f"""
# In this lesson we are going over how to create dashboards using Streamlit.
# First, we will go over how to present information through dashboards. Second,
# add a Machine Learning model for easy use by external customers.
# """

# st.write(txt)
#
#
# df = pd.read_csv("data/titanic.csv")
#
# st.dataframe(df.head())
#
#
# st.table(df.describe())
#
#
# st.bar_chart(df, x="pclass", y="fare", color="survived")
#
# chart = alt.Chart(df).mark_bar().encode(
# x="pclass", y="fare", color="survived"
# ).interactive()
#
# st.altair_chart(chart)

