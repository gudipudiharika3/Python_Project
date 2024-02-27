# StudentManagement.py
from Student_database import Student, create_database
from AddStudent import addStudent
from Delete import delete_student
from Modify import update_student_information
from query_Student import query_student_scores


class StudentManagement:
    def __init__(self):
        # Create an engine to connect to the database (students.db)
        self.session = create_database()

    def show_students(self):
        print("Select an option to display student records:")
        print("\u2666 1. Show all students")
        print("\u2666 2. Show students by name")
        print("\u2666 3. Show students by ID")
        print('\u2666 Other Return')

        option = input("Enter your choice (1-3): ")
        if option == '1':
            self.show_all_students()
        elif option == '2':
            self.show_students_by_name()
        elif option == '3':
            self.show_students_by_id()
        else:
            print("\u274C  Returning to the previous menu.")

    def show_all_students(self):
        all_students = self.session.query(Student).all()

        if not all_students:
            print("\u274C No student existing.")
            return

        self.print_student_records(all_students)

    def show_students_by_name(self):
        name = input("Please Enter Student Name to Display: ")
        found_students = self.session.query(Student).filter(Student.name.ilike(f"%{name}%")).all()

        if not found_students:
            print("\u274C No matching student records found.")
            return

        self.print_student_records(found_students)

    def show_students_by_id(self):
        student_id = int(input("Enter the student ID to Display: "))
        student = self.session.query(Student).filter_by(id=student_id).first()

        if not student:
            print("\u274C No student found with the given ID.")
            return

        self.print_student_records([student])

    def print_student_records(self, students):
        print("========================== Student Records ==========================================")
        print(f"{'ID':<11}{'Name':<20}{'Age':<5}{'Gender':<8}{'Major':<10}{'Phone':<15}")
        print('-' * 70)
        for student in students:
            print(f"{student.id:<11}{student.name:<20}{student.age:<5}{student.gender:<8}{student.Major:<10}{student.phone:<15}")



    def add_student(self):
        # Implement functionality to add a student record
        addStudent()

    def modify_student(self):
        # Implement functionality to modify student details
        update_student_information()

    def delete_student(self):
        # Implement functionality to delete a student record
        delete_student()

    def query_student_scores(self):
        # Implement functionality to query a student record
        query_student_scores()

    def print_student_menu(self, username):
        while True:
            with open('student.txt', "r", encoding="utf-8") as file:
                student_menu = file.read()
                user_menu = student_menu.replace("%s", username)
                print(user_menu)
                text = input("Please select (1 - 6):")
                if text == "1":
                    self.add_student()
                if text == "2":
                    self.show_students()
                if text == "3":
                    self.modify_student()
                if text == "4":
                    self.delete_student()
                if text == "5":
                    self.query_student_scores()
                if text == "6":
                    ex = input("Do you want to exit the system? Enter y to confirm: ")
                    if ex == "y":
                        print("Exit the system...")
                        return


# Usage example
student_manager = StudentManagement()
