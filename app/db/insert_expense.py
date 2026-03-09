from app.db.connection import get_connection

def insert_expense(expense):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (date, category, amount, description)
        VALUES (%s, %s, %s, %s)
        """,
        (expense.date, expense.category, expense.amount, expense.description)
    )

    conn.commit()
    cursor.close()
    conn.close()