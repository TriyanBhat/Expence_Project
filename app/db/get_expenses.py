from app.db.connection import get_connection

def fetch_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, date, category, amount, description FROM expenses")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows