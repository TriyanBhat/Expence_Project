from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
        date: date
        category: str
        amount: float
        description: str