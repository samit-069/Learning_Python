import json

class StudentManager:
    def __init__(self, file_name="students.json"):
        self.students = []
        self.file_name = file_name
        self.load_students()

    def load_students(self):
        try:
            with open(self.file_name, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = []

    def save_students(self):
        with open(self.file_name, "w") as file:
            json.dump(self.students, file)

    def add_student(self):
        while True:
            roll = input("Enter roll number of student: ")
            if roll.isdigit():
                roll = int(roll)
                break
            else:
                print("Not a number")

        name = input("Enter name of student: ")

        while True:
            marks = input("Enter marks of student: ")
            if marks.isdigit():
                marks = int(marks)
                break
            else:
                print("Not a number")

        self.students.append({
            "roll": roll,
            "name": name,
            "marks": marks
        })

        self.save_students()

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print(f"Roll no.: {student['roll']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print("-" * 20)

    def search_student(self):
        while True:
            ser_rol = input("Enter roll number of student to search: ")
            if ser_rol.isdigit():
                ser_rol = int(ser_rol)
                break
            else:
                print("Not a number")

        found = False
        for student in self.students:
            if student['roll'] == ser_rol:
                print(f"Roll no.: {student['roll']}")
                print(f"Name: {student['name']}")
                print(f"Marks: {student['marks']}")
                print("-" * 20)
                found = True
                break

        if not found:
            print("Roll Number doesn't exist")

    def cal_avg(self):
        if not self.students:
            print("No students found.")
            return

        total = 0
        for student in self.students:
            total += student['marks']

        avg = total / len(self.students)
        print(f"Average of class is: {avg:.2f}")
