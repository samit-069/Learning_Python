#Day 5 project
#simple contact book with add, delete, search function

contact = {}
def add_contact():
    name= input("Enter name: ")
    number= int(input("Enter number: "))
    email= input("Enter email: ")
    
    contact[name] = {
        "number": number,
        "email": email
    }

def view_all():
    for name, details in contact.items():
        print(f"Name: {name}")
        print(f"Number: {details['number']}")
        print(f"Email: {details['email']}")


def search_contact():
    search = input("Enter name to be searched: ")
    if search in contact:
        print(f"Name: {search}")
        print(f"Number: {contact[search]['number']}")
        print(f"Email: {contact[search]['email']}")
    else:
        print("Contact not found")

def delete_contact():
    delete_name = input("Enter name to be deleted: ")
    if delete_name in contact:
        del contact[delete_name]
    else:
        print("Contact not found")

while True:
    print("Menu:")
    print("select from 1-5")
    print("1.Add Contact")
    print("2.View All Contact")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")
    menu_sel = int(input("Enter number to selecct menue(1-5)"))
    if menu_sel == 1:
        add_contact()
    elif menu_sel == 2:
        view_all()
    elif menu_sel == 3:
        search_contact()
    elif menu_sel == 4:
        delete_contact()
    elif menu_sel == 5:
        print("Thank you for using Contact_Book")
        break
    else:
        print("Invalid number")
        