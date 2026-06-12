import streamlit as st
import datetime

#Title
st.title("Age Calculator")

min_date = datetime.date(1900,1,1)
max_date = datetime.date.today()
default_date = datetime.date(max_date.year-18, max_date.month, max_date.day)

dob = st.date_input("Enter your DOB: ",value= default_date, min_value= min_date, max_value= max_date)

curr_date = datetime.date.today()
age =  curr_date.year - dob.year

st.write(f"Your age is: {age}")