from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from pydantic import BaseModel
from typing import List

class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class Date_Range(BaseModel):
    start_date: date
    end_date: date

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expense(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code= 404, detail="failed to load  expenses")
    return expenses

@app.post("/expenses/{expense_date}")
def add_expense(expense_date:date ,expenses: List[Expense] ):
    for expense in expenses:
        db_helper.add_expenses_for_date(expense_date, expense.amount, expense.category, expense.notes)

    return  {"expense update successfully"}


@app.post("/analytics/")
def get_analytics(date_range: Date_Range):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code= 404, detail="failed to load  expense summary")

    total =0
    final_response = {}
    for row in data:
        total += row["total"]

    for row in data:
        percentage = (row["total"]/total)*100
        final_response[row["category"]] = {
            "total":row["total"],
            "percentage":round(percentage,1)
        }
    return final_response