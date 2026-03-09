import csv
from app.db.get_expenses import fetch_expenses


def export_csv():

    rows = fetch_expenses()

    headers = ["ID", "Date", "Category", "Amount", "Description"]

    with open("exported_expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(headers)

        writer.writerows(rows)

    print("Data exported to exported_expenses.csv")