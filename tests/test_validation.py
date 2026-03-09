from app.validation.expense_schema import Expense

def test_expense_schema():

    expense = Expense(
        category="Food",
        amount=100,
        date="2024-01-01",
        description="Lunch"
    )

    assert expense.category == "Food"
    assert expense.amount == 100