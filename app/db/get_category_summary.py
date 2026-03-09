from app.db.connection import get_connection


def fetch_category_summary():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows