import streamlit as st
# We will learn how to use widgets here, and conditional interaction also
# widgets are elements we use to interact with the Application

st.title("Chai Maker App") # title/heading
st.subheader("Make your own chai") # subheading

# text_input
name = st.text_input("Please enter your Name: ")
if name:
    st.write(f"Welcome {name}!")
    
# date_input (calender)
dob = st.date_input("Enter your DOB: ", value = "today") # takes date as input, with today's date as default
st.write(f"Your Date of Birth is {dob}")

# number_input
cups = st.number_input("How many cups do you want?", min_value=1, max_value=10)
if cups:
    st.write(f"You want {cups} cups of Chai!")
    
# selectbx (drop down)
flavour = st.selectbox("What flavour would you like?", ["Simple", "Adrak", "Elaichi", "Tulsi"])
if flavour:
    st.write(f"Your chosen flavout is: {flavour}")

# Radio buttons
base = st.radio("Which chai base would you like?", ["Almond Milk", "No-lactos milk", "water"])
if base:
    st.write(f"Your chai base is {base}")
    
# Slider
sugar = st.slider("How many spoons of sugar would you like?", 0, 5, 2) # min_val, max_val, default_val
if sugar:
    st.write(f"You have added {sugar} spoons of sugar")
    
# CheckBox
options = ["Extra Masala", "Extra Milk", "Extra Chai Patti"]
add_ons = []
for option in options:
    if st.checkbox(option):
        add_ons.append(option)
if add_ons:
    st.write(f"Your add on are: {add_ons}")


if st.button("Make Chai"): # button -> widget
    st.success("Your Chai is being brewed") # if we click on button -> we get a SUCCESS msg