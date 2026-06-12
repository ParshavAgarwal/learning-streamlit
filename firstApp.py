import streamlit as st

#Heading / Title
st.title("Hello Language App")
#Subheading
st.subheader("What is your Favorite Programming Language?")
#Text
st.text("There are many programming languages out there, but which one is your favorite?")
#write
st.write("Select your favorite programming language from the options below:")
# there is not much diff in text and write.

#Selectbox 
language = st.selectbox("Select your favorite programming language!", ["Python", "JavaScript", "Java", "C++", "Other"])
#Display the selected language
st.write(f"Your favorite programming language is: {language}. Excellent choice!!")