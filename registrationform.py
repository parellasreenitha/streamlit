import streamlit as st
import time 
st.title("REGISTRATION FORM");
st.write("DETAILS");
name=st.text_input("First name")
name=st.text_input("Last name")
email=st.text_input("Email/Gmail")
name=st.text_input("Phone number")
age=st.number_input("age",step=1)
password=st.text_input("Password",type="password")
text=st.text_area("Addition info information")
st.button("Submit")
st.snow()
st.balloons()