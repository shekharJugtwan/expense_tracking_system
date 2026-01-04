import streamlit as st
from datetime import datetime
import requests


API_URL = "http://127.0.0.1:8000/"

def add_update_tab():
    selected_date = st.date_input("Select date", datetime(2024, 8, 2), label_visibility="collapsed")
    date_key = selected_date.isoformat()
    response = requests.get(f"{API_URL}expenses/{selected_date}")
    if response.status_code == 200:
        existing_expense = response.json()
    else:
        st.write("Something went wrong")
        existing_expense = []
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other", "footwear"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            col1.subheader("Amount")
        with col2:
            col2.subheader("Category")
        with col3:
            col3.subheader("notes")

        expenses = []

        for i in range(10):
            if i < len(existing_expense):
                amount = existing_expense[i].get("amount", 0.0)
                category = existing_expense[i].get("category", "Other")
                notes = existing_expense[i].get("notes", "")
            else:
                amount = 0.0
                category = "Other"
                notes = ""

            if category not in categories:
                updated_categories = categories + [category]
            else:
                updated_categories = categories

            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, max_value=10000.0, value=amount,
                                               key=f"{date_key}amount{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="category", options=updated_categories,
                                              index=updated_categories.index(category), key=f"{date_key}category{i}",
                                              label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"{date_key}notes{i}",
                                            label_visibility="collapsed")

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input,
            })
            print("new line")
            print(expenses)
        submitted = st.form_submit_button("Submit")

        if submitted:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0.0]

            requests.post(f"{API_URL}expenses/{selected_date}", json=filtered_expenses)