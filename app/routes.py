from fastapi import APIRouter, HTTPException, Depends, Query
from app.models import Expenses
from datetime import date

import hashlib
import time

router = APIRouter()


@router.get("/expenses")
async def get_expenses():
    expenses = await Expenses.all().order_by("-date")
    return [
        {
            "id": e.id,
            "amount": e.amount,
            "category": e.category,
            "description": e.description,
            "date": e.date.isoformat()
        }
        for e in expenses
    ]

@router.get("/expenses/stats")
async def get_stats():
    expenses = await Expenses.all()

    total = sum(e.amount for e in expenses)

    by_cat = {}
    for e in expenses:
        by_cat[e.category] = by_cat.get(e.category, 0) + e.amount

    return {
        "total": total,
        "by_category": by_cat
    }


@router.post("/expenses")
async def add_expenses(data: dict):
    try:
        expense = await Expenses.create(
            amount=data['amount'], 
            category=data['category'],
            description=data.get("description"),
            date=data["date"]
        )
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e.args[0]}")

    return {'id': expense.id, 'message':'Expense created'}


@router.put('/expenses/{id}')
async def update_expense(expense_id: int, data: dict):
    expense = await Expenses.get_or_none(id=expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    expense.amount = data.get("amount", expense.amount)
    expense.category = data.get("category", expense.category)
    expense.description = data.get("description", expense.description)
    expense.date = data.get("date", expense.date)
    await expense.save()

    return {"msg": "Expense updated"}


from fastapi import Path

@router.delete("/expenses/{expense_id}")
async def delete_expense(expense_id: int = Path(...)):
    expense = await Expenses.get_or_none(id=expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    await expense.delete()
    return {"msg": "Expense deleted"}


@router.get("/expenses")
async def get_expenses_f(
    start: date = Query(None), 
    end: date = Query(None), 
):
    q = Expenses.all()

    if start:
        q = q.filter(date__gte=start)
    if end:
        q = q.filter(date__lte=end)

    expenses = await q.order_by("-date")

    return [
        {
            "id": e.id,
            "amount": e.amount,
            "category": e.category,
            "description": e.description,
            "date": e.date.isoformat()
        }
        for e in expenses
    ]
