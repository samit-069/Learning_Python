import json
import student_manager

def show_menu():
    manager = student_manager.StudentManager()
    while True:
        print("Menu:")
        print("1.Add Student")
        print("2.View All Student")
        print("3.Search Student")
        print("4.Calculate class average")
        print("5.Exit")

        menu_sel = input("Enter from 1-5 to select from menu: ")
        try:
            menu_sel = int(menu_sel)
            if menu_sel == 1:
                manager.add_student()
            elif menu_sel == 2:
                manager.view_students()
            elif menu_sel == 3:
                manager.search_student()
            elif menu_sel == 4:
                manager.cal_avg()
            elif menu_sel == 5:
                print("-" * 20)
                break
            else:
                print("outside menu number range")
        except ValueError:
            print("Invalid value, please enter NUMBER from 1-5")