import streamlit as st
import requests

st.title("Live Currency Converter")

# Amount input
amount = st.number_input("Enter the Amount in INR: ", min_value= 1)

# SelectBox -> converted to??
target_currency = st.selectbox("In which currency would you like to convert?", ["USD", "EUR", "JPY", "AED"])

if st.button("Convert"):
    # url se response lenge
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    
    if response == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted_amt = rate * amount
        st.success(f"{amount} INR = {converted_amt:.2f} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")