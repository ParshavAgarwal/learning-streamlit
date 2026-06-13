import streamlit as st
import pandas as pd

st.title("Sample Dashboard")

#Let's play with CSV
file = st.file_uploader("Upload your csv file:", type="csv")

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df) # used to displat the data in table format
    
if file:
    st.subheader("Data Description")
    st.write(df.describe())
    
if file:
    authors = df["Author"].unique()
    selected_author = st.selectbox("Filter Book by authors", options=authors)
    filtered_data = df[df["Author"] == selected_author] # jaha bhi y condition true hain -> vo data(vo rows) 'filtered_data' m store ho jayega
    st.subheader("Filtered data")
    st.dataframe(filtered_data)