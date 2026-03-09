from app.db.connection import get_connection

def create_expenses_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id SERIAL PRIMARY KEY,
        date DATE,
        category VARCHAR(100),
        amount FLOAT,
        description TEXT
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Expenses table created!")

if __name__ == "__main__":
    create_expenses_table()