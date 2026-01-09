import streamlit as st
from datetime import datetime
import requests
from datetime import date
import pandas as pd

def analytics_by_month():
    st.title("Expense Breakdown by Months")
    response = requests.get("http://127.0.0.1:8000/analytics_by_month")
    if response.status_code == 200:
        existing_expense = response.json()

        #isinstance is use to check if the data is of perticular type to we are checking here the data as to
        # a dictionary or not and if yes then making the list of the values of the dictionary not the keys only value.
        if isinstance(existing_expense, dict):
            existing_expense = list(existing_expense.values())

        df = pd.DataFrame(existing_expense)
        # st.dataframe(df,use_container_width = True)
        result = (df.rename(columns = {

                                                    "ym": "Months",
                                                    "total": "Total"
        }))

        st.bar_chart(data = result.set_index("Months")['Total'], use_container_width = True)
        st.table(result)
