# app.py
import streamlit as st
import auth  # your auth module

st.set_page_config(page_title="Dr Cartoon", page_icon="📺")

# Protect the app
auth.require_login()

# If user is logged in
st.success(f"Welcome {st.session_state.user['email']}")
st.image(st.session_state.user["picture"], width=100)
st.write("User info:")
st.json(st.session_state.user)

# Your actual app logic here
st.write("🎉 This is your secure app content.")
