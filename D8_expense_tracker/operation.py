#operation.py
import json
import storage


def add_expenses():
    amount = int(input("Enter expense amount:Rs "))
    catogery = input("Enter catogery of expense: ")
    note = input("Note: ")

    storage.expenses.append({
        "amount" : amount,
        "catogery" : catogery,
        "note" : note
    })

def view_expenses():
    for expense in storage.expenses:
        print(f"amount: Rs{expense['amount']}")
        print(f"catogery: {expense['catogery']}")
        print(f"note: {expense['note']}")

def total_expenses():
    total_sum = 0
    for expense in storage.expenses:
        total_sum += expense["amount"]
    print(f"Grand Total of all your expenses is: {total_sum}")


