#menu.py
import json
import storage
import operation

def show_menu():
    while True:
        print("Menu:")
        print("1.Add Expense")
        print("2.View All Expense")
        print("3.Total Expense")
        print("4.Exit")

        sel_m = int(input("select from menu (1-4)"))
        if sel_m == 1:
            operation.add_expenses()
            storage.save_expenses()
        elif sel_m == 2:
            operation.view_expenses()
        elif sel_m == 3:
            operation.total_expenses()
        elif sel_m == 4:
            print("Thank you for using Expense Tracker!!")
            break
        else:
            print("Invalid number, Please select from 1-4")