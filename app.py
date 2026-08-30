import streamlit as st

st.title("Circle Area Calculator")

value = st.number_input("Enter your radius:", min_value=0.0)

area = 3.14 * value * value

st.write("Area is:", area)