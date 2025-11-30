#Day3 Project
task=[]

def add_task(a_task):
    return task.append(a_task)
def show_task(task):
    print(task)
def remove_task(r_task):
    return task.remove(r_task)
i=0

while i<4:
    print("(select from 1-4)Menu:")
    print("1.Add task")
    print("2.Show task")
    print("3.Remove task")
    sel_menu=int(input("4.Exit"))
    if sel_menu == 1:
        a_task = input("Add task:")
        add_task(a_task)
        i=1
    elif sel_menu == 2:
        show_task(task)
        i=2
    elif sel_menu == 3:
        r_task = input("Remove task:")
        remove_task(r_task)
        i=3
    else:
        i=4