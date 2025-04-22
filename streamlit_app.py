import streamlit as st
import requests

st.set_page_config(page_title="AI Portfolio Generator", page_icon="🚀", layout="wide")

import my_portfolios

st.title("🚀 AI Portfolio Generator")

# The backend URL on Render
BACKEND_URL = "https://auto-resume-portfolio.onrender.com"

st.write("Click the button below to check the backend status:")

# Check on load (root path)
try:
    res = requests.get(f"{BACKEND_URL}/", timeout=3)
    if res.ok:
        st.success("✅ Backend is live and responding.")
    else:
        st.warning("⚠️ Backend responded with a non-200 status.")
except Exception as e:
    st.warning(f"⚠️ Could not reach backend: {e}")

# Button check also uses root path
if st.button("Check Backend Again"):
    try:
        res = requests.get(f"{BACKEND_URL}/", timeout=3)
        if res.ok:
            st.success("✅ Backend is healthy!")
        else:
            st.error("❌ Backend returned an error.")
    except Exception as e:
        st.error(f"Could not reach backend: {e}")

my_portfolios.main()
