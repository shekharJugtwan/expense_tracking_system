import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logging

logger = setup_logging('db_helper')


@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f"running fetch_expenses_for_date is called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date is called with {expense_date}")

    with get_db_cursor() as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def add_expenses_for_date(expense_date, amount, category, notes):
    logger.info(f" add_expenses_for_date is called with {expense_date}{amount}{category}{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)", (expense_date, amount, category, notes))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"running fetch_expense_summary is called with {start_date}{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            ''' SELECT category, SUM(amount) as total
            FROM expenses WHERE expense_date BETWEEN %s and %s 
            GROUP BY category;''', (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

def fetch_expenses_by_months():
    logger.info(f"running fetch_expenses_by_month is called ")
    with get_db_cursor() as cursor:
        cursor.execute(''' SELECT 
                            DATE_FORMAT(expense_date, '%Y-%m') AS ym, 
                                  SUM(amount) AS total 
                            FROM expenses 
                            GROUP BY DATE_FORMAT(expense_date, '%Y-%m')
                            ORDER BY ym; ''')
        data = cursor.fetchall()
        return data


if __name__ == '__main__':

    # expenses = fetch_expenses_for_date('2024-08-1')
    # for expense in expenses:
    #     print(expense)
    add_expenses_for_date("2025-12-19", 1060, "credit card bill", "paid my credit card")
