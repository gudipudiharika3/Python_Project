"""
Delete Page
"""

from Student_database import create_database, Student


def delete_student():
    print("=============================== Delete Student ==========================")
    print("\u2666 1. Delete by student name")
    print("\u2666 2. Delete by student id")
    print("\u2666 3. Other Return")

    option = input("Enter your choice (1-3): ")
    if option == '2':
        delete_student_by_id()
    elif option == '1':
        delete_student_by_name()
    else:
        return


def delete_student_by_id():
    session = create_database()

    # Input student ID to delete
    student_id = input("Enter the student ID to delete: ")

    # Check if the student exists
    student = session.query(Student).filter_by(id=student_id).first()

    if not student:
        print("No student found with the given ID.")
        return
    print("========================== Student Records ==========================================")
    print(f"{'ID':<11}{'Name':<20}{'Age':<5}{'Gender':<8}{'Major':<10}{'Phone':<15}")
    print('-' * 70)
    print_student_record(student)

    confirmation = input(f"Are you sure you want to delete student ID {student_id}? (yes/no): ")
    if confirmation.lower() == 'yes':
        session.delete(student)
        session.commit()
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def delete_student_by_name():
    session = create_database()

    # Input student name to delete
    student_name = input("Enter the student name to delete: ")

    # Check if the student exists
    students = session.query(Student).filter_by(name=student_name).all()

    if not students:
        print("No student found with the given name.")
        return
    print("========================== Student Records ==========================================")
    print(f"{'ID':<11}{'Name':<20}{'Age':<5}{'Gender':<8}{'Major':<10}{'Phone':<15}")
    print('-' * 70)
    for student in students:
        print_student_record(student)

    confirmation = input(f"Are you sure you want to delete student {student_name}? (yes/no): ")
    if confirmation.lower() == 'yes':
        session.query(Student).filter_by(name=student_name).delete()
        session.commit()
        print("Student(s) deleted successfully.")
    else:
        print("Deletion cancelled.")


def print_student_record(student):

    print(f"{student.id:<11}{student.name:<20}{student.age:<5}{student.gender:<8}"
          f"{student.Major:<10}"f"{student.phone:<15}")

