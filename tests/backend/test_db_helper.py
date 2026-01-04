from backend import db_helper

def test_fetch_expenses_for_date():
    expense = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expense) == 1