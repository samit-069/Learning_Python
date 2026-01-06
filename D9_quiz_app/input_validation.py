#input_validation.py
def get_user_choice(num_options):
    while True:
        sel = input("Enter choice: ")
        try:
            sel = int(sel)
            if sel not in range(1, num_options+1):
                print(f"Enter a number from 1 to {num_options}")
            else:
                return sel
        except ValueError:
            print(f"Please enter a number from 1 to {num_options}")
