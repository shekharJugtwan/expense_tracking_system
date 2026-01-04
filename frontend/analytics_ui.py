import streamlit as st
from datetime import datetime
import requests
from datetime import date
import pandas as pd

API_URL = "http://127.0.0.1:8000/"

def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", value = date.today())
    with col2:
        end_date = st.date_input("End date", value = date.today())

    if st.button("Get Analytics"):
        payload = {
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        print(payload)
        response = requests.post(f"{API_URL}analytics/", json = payload)
        data = response.json()

        df = pd.DataFrame(data)
        st.dataframe(df,use_container_width = True)
        st.title("Expense breakdown by Category")

        result = (df.T.reset_index().rename(columns = {"index": "category",
                                                       "total": "Total",
                                                       "percentage": "Percentage"}))

        df_sorted = result.sort_values(by = "Percentage",ascending = False)
        st.bar_chart(data = df_sorted.set_index("category")['Percentage'], use_container_width = True)

        st.table(df_sorted)