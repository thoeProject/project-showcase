import streamlit as st
import pandas as pd

st.set_page_config(page_title="Todo App", page_icon=":tada:", layout = "wide")
content = pd.read_csv("data.csv", sep=";")

col1, col2 = st.columns(2)

# 2 first columns
with col1:
    st.image("images/todo-image.png")

with col2:
    st.title("Todo App")
    des = """
        This is an app to track your task regularly!!!"""
    st.info(des)

# next 2 colums
col3, col4 = st.columns(2)
for index, row in content[:2].iterrows():
    with col3:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

for index, row in content[2:].iterrows():
    with col4:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])


