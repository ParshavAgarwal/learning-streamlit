import streamlit as st

# Taiking Name and Age, etc in sidebar
name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", min_value= 10)

#Title ---------------------------------------------------------------------------
st.title("Coffie Cup House")
if name:
    st.subheader(f"Welcome {name} to CCH! Please place your order.")

# Main ordering --------------------------------------------------------------------    
order = st.selectbox("Which coffe would you like?", ["Hot", "Cold", "Black"])
if order:
    st.write(f"You have chosen {order} coffee.")

if st.button("Place the order"):
    st.success("Your coffee is being brewed.")

st.divider() #Line break / Horizontal line --------------------------------------------------

#markdown ---------------------------------------------------------------------------------
st.markdown("### You can Vote in you mean time")
st.markdown('> Blockquote')

chai_votes = 0
coffee_votes = 0

#Columns -------------------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1: #col 1 k andar ka maal masala
    st.header("Chai")
    st.image("https://th.bing.com/th/id/OIP.FjNWl0STMMidMMHPYyJ2ZQHaHa?w=190&h=190&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3", width= 150)
    
    if st.button("Vote for Chai"):
        chai_votes += 1
        st.write(f"Chai has {chai_votes} votes")

with col2: #col 2 k andar ka maal masala
    st.header("Coffee")
    st.image("https://tse3.mm.bing.net/th/id/OIP.8q8wUN4bfvH9a6p8ukJiSAHaHa?rs=1&pid=ImgDetMain&o=7&rm=3", width= 150)
    
    if st.button("Vote for Coffee"):
        coffee_votes += 1
        st.write(f"Chai has {coffee_votes} votes")
        
st.divider()

# Expander ----------------------------------------------------------------------------------
with st.expander("BTS of your perfect coffee"):
    st.write("""
    1. Take out coffee beans
    2. clean and grind them
    3. Liquidify them
    4. Add Milk         
    """)