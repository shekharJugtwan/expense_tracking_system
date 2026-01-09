import streamlit as st
from datetime import datetime
import requests
from add_update_ui import add_update_tab
from analytics_by_category import analytics_by_category
from analytics_by_month import analytics_by_month

API_URL = "http://127.0.0.1:8000/"

st.title("Expense Tracking system")
tab1, tab2, tab3 = st.tabs(["Add/Update", "analytics_by_category","analytics_by_month"])

with tab1:
    add_update_tab()
with tab2:
    analytics_by_category()
with tab3:
    analytics_by_month()