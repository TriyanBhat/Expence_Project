from app.db.connection import get_connection


def fetch_total():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total