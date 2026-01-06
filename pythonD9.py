#Day 9
#Input Validation and Error Handeling

#Task 1: Safe number input


while True:
    num = input("Enter a number")
    check = num.isdigit()
    if check == True:
        num = int(num)
        print(f"{num} is a number")
        break
    else:
        print("Not a number")

#Task 2: menu validation

while True:
    print("Menu:")
    print("select from 1-5")
    print("1.Add Contact")
    print("2.View All Contact")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")
    sel_men = input("select from menu")
    try:
        sel_men = int(sel_men)
        if sel_men == 1:
            print("contact added")
        elif sel_men == 2:
            print("contact viewed")
        elif sel_men == 3:
            print("contact searched")
        elif sel_men == 4:
            print("contact deleted")
        elif sel_men == 5:
            print("Thank you for using Contact_Book")
            break
        else:
            print("Enter from 1-5")
    except ValueError:
        print("Invalid value, please enter NUMBER from 1-5")