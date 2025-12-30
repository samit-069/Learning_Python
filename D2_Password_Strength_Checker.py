#Day 2 project

password = input("Enter you Password: ")
lenght = len(password)
has_upper = False
has_lower = False
has_number = False
has_Special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_number = True
    else:
        has_Special = True
if lenght>=8 and has_upper==True and has_lower==True and has_number==True and has_Special==True:
    print("You have STRONG Password")
else:
    print("You're Password is WEAK!!")