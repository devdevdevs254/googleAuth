import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
import os
from urllib.parse import urlencode

# Load secrets from Streamlit secrets manager
client_id = st.secrets["client_id"]
client_secret = st.secrets["client_secret"]
redirect_uri = st.secrets["redirect_uri"]

authorization_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"
token_endpoint = "https://oauth2.googleapis.com/token"
userinfo_endpoint = "https://openidconnect.googleapis.com/v1/userinfo"

if "user" not in st.session_state:
    st.session_state.user = None

def handle_callback():
    params = st.query_params.to_dict()
    if "code" in params:
        client = OAuth2Session(client_id, client_secret, redirect_uri=redirect_uri)
        token = client.fetch_token(token_endpoint, code=params["code"])
        userinfo = client.get(userinfo_endpoint, token=token).json()
        st.session_state.user = userinfo

def login():
    auth_url = authorization_endpoint + "?" + urlencode({
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    })
    st.markdown(f"[Click here to login with Google]({auth_url})")

st.title("🔐 Google Login Example")

if st.session_state.user:
    st.success(f"Welcome {st.session_state.user['email']}")
    st.json(st.session_state.user)
else:
    handle_callback()
    login()
