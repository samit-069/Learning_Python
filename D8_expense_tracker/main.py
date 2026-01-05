#main.py
import json
import menu
import operation
import storage

storage.load_expenses()
menu.show_menu()