import streamlit as st
from datetime import datetime
import requests
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab

API_URL = "http://127.0.0.1:8000/"

st.title("Expense Tracking system")
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()