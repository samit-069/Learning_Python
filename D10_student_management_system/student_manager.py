import json

class StudentManager:
    def __init__(self, file_name="students.json"):
        self.file_name = file_name
        self.students = {}
        self.load_students()

    def load_students(self):
        try:
            with open(self.file_name, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = {}

    def save_students(self):
        with open(self.file_name, "w") as file:
            json.dump(self.students, file)

    def add_student(self):
        while True:
            roll = input("Enter roll number of student: ")
            if roll.isdigit():
                roll = int(roll)
                if roll in self.students:
                    print("Roll number exists!!")
                else:
                    break
            else:
                print("Not a number")
        while True:
            name = input("Enter name of student: ")
            if len(name) == 0:
                print("Please enter name")
            else:
                break

        while True:
            marks = input("Enter marks of student: ")
            if marks.isdigit():
                marks = int(marks)
                break
            else:
                print("Not a number")

        self.students[roll]={
            "name": name,
            "marks": marks
        }
        self.save_students()

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for roll, data in self.students.items():
            print(f"Roll no.: {roll}")
            print(f"Name: {data['name']}")
            print(f"Marks: {data['marks']}")
            print("-" * 20)

    def search_student(self):
        while True:
            ser_rol = input("Enter roll number of student to search: ")
            if ser_rol.isdigit():
                ser_rol = int(ser_rol)
                break
            else:
                print("Not a number")

        if ser_rol in self.students:
            print(f"Roll no.: {ser_rol}")
            print(f"Name: {self.students[ser_rol]['name']}")
            print(f"Marks: {self.students[ser_rol]['marks']}")
            print("-" * 20)                   
        else:
            print("Roll Number doesn't exist")

    def cal_avg(self):
        if not self.students:
            print("No students found.")
            return

        total = 0
        for data in self.students.values():
            total += data['marks']

        avg = total / len(self.students)
        print(f"Average of class is: {avg:.2f}")
