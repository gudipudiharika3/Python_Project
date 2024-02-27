from Student_database import create_database, Student
import re


def update_student_information():
    session = create_database()  # Creating the database session

    print('============================== Modify Records ============================')

    # Input student ID to update
    student_id = input("Enter the student ID to update: ")

    # Query the student record to update
    student = session.query(Student).filter_by(id=student_id).first()

    if not student:
        print("\u274C No Existing records")
        return

    print_student_record(student)

    # Update student's age
    new_age = input("Enter the new age (please Enter without modification): ")
    if new_age != '':
        while not validate_age(new_age):
            print("\u274C  Invalid age.")
            new_age = input("Enter the new age (please Enter without modification):")

        student.age = int(new_age)


    # Update student's major
    new_major = input("Enter the new major (please Enter without modification): ")
    if new_major != '':
        while not new_major.replace(' ', '').isalpha():
            print("\u274C Invalid major.")
            new_major = input("Enter the new major (please Enter without modification): ")

        student.Major = new_major


    # Update student's phone number
    new_phone = input("Enter the new phone number (xxx-xxx-xxxx) (please Enter without modification): ")
    if new_phone != '':
        while not validate_phone(new_phone):
            print("\u274C Invalid phone number.")
            new_phone = input("Enter the new phone number (xxx-xxx-xxxx) (please Enter without modification): ")

        student.phone = new_phone
        session.commit()

    print("\u2714 Record Modified successfully.")


def validate_age(age):
    return age.isdigit() and 0 <= int(age) <= 100


def validate_phone(phone):
    return re.match(r'^\d{3}-\d{3}-\d{4}$', phone)


def print_student_record(student):
    print("========================== Student Records ==========================================")
    print(f"{'ID':<11}{'Name':<20}{'Age':<5}{'Gender':<8}{'Major':<10}{'Phone':<15}")
    print('-' * 70)
    print(f"{student.id:<11}{student.name:<20}{student.age:<5}{student.gender:<8}{student.Major:<10}"
          f"{student.phone:<15}")

