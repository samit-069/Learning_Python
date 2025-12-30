#Dictionary
#example:
student={
    "name": "Samit",
    "age": 20,
    "is_student": "True"
}
#Accessing values:
print(student)

print(student["name"])
print(student["age"])

#update and adding:

student["name"]= "Samit_Maharjan"
student["age"]= 21

print(student["name"])
print(student["age"])

#Removing Data:
del student["is_student"] #or student.pop("is_student")

print(student)

#looping throug dictionary
#key only:
for key in student:
    print(key)

#values only:
for value in student.values():
    print(value)

#key+values:
for key, value in student.items():
    print(key,value)


#mini exercise create dictionary for user

user ={
    "user_name": input("Enter your name: "),
    "email": input("Enter you email: "),
    "age": int(input("Enter your age: "))
}

for key, value in user.items():
    print(key, value)