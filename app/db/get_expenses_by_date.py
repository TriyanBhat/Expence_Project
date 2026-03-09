from app.db.connection import get_connection


def fetch_expenses_by_date(date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE date = %s",
        (date,)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows