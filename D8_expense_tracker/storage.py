#storage.py
import json
expenses = []

def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses, file)
def load_expenses():
    global expenses
    try:
        with open("expenses.json","r") as file:
            expenses = json.load(file)
    
    except FileNotFoundError:
        print("File not found, Creating new file")
        expenses = []