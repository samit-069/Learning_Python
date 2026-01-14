import blog_manager

def show_menu():
    manager = blog_manager.BlogManager()
    while True:
        print("\nMenu:")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Post")
        print("4. Delete Post")
        print("5. Exit")

        menu_sel = input("Enter 1-5 to select from menu: ")
        try:
            menu_sel = int(menu_sel)
            if menu_sel == 1:
                manager.create_post()
            elif menu_sel == 2:
                manager.view_post()
            elif menu_sel == 3:
                manager.search_post()
            elif menu_sel == 4:
                manager.delete_post()
            elif menu_sel == 5:
                print("-" * 20)
                break
            else:
                print("Outside menu number range")
        except ValueError:
            print("Invalid value, please enter NUMBER from 1-5")
