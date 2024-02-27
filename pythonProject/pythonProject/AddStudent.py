"""
Add Student
"""

import re
from Student_database import create_database, Student, Score


def addStudent():
    session = create_database()  # Creates the database session

    print('=============================== Add Student ============================ ')
    print('1. The first letter of firstname and lastname must be capitalized')
    print('2. Firstname and lastname must each have at least two letters')
    print('3. No digit allowed in the name')
    print('4. Age must between 0 and 100')
    print('5. Gender can be M (Male), F (Female) or O (Other)')
    print('6. Phone must be in the (xxx-xxx-xxxx) format')

    while True:
        full_name = input("Enter student's full name (Firstname Lastname): ")
        first_name, last_name = extract_first_last_name(full_name)

        if not validate_name(first_name):
            print("\u274C Invalid first name.")
            continue

        if not validate_name(last_name):
            print("\u274C Invalid last name.")
            continue

        while True:
            age = input("Enter student's age: ")
            if validate_age(age):
                break
            else:
                print("\u274C Invalid age.")

        while True:
            gender = input("Enter student's gender (M/F/O): ")
            if validate_gender(gender):
                break
            else:
                print("\u274C Invalid gender.")

        Major = input("Please Enter Student's Major:")

        while True:
            phone = input("Enter student's phone number (xxx-xxx-xxxx): ")
            if validate_phone(phone):
                break
            else:
                print("\u274C Invalid phone number.")

        Student_id = generate_unique_id(session)

        new_student = Student(id=Student_id, name=full_name, age=int(age), gender=gender, Major=Major, phone=phone)
        new_score = Score(name=full_name, CS1030=0, CS1100=0, CS2030=0)
        new_student.score.append(new_score)
        session.add(new_student)
        session.commit()
        print("\u2714 Student added successfully!")
        break
    while True:
        print('\u2666 1.Continue')
        print('\u2666 2.exit')
        more_students = input("Please select 1 or 2:")                                                                                                                                                       
        if more_students == '1':
            addStudent()
        elif more_students == '2':
            print("Returning to the previous menu.")
            break
        else:
            print("\u274C Invalid input. Please enter 'yes' or 'no'.")


def generate_unique_id(session):
    prefix = '70030'

    # Fetch the last student ID from the database and increment the last 6 digits
    last_student = session.query(Student).order_by(Student.id.desc()).first()
    if last_student:
        last_id = int(last_student.id[6:])  # Extract numeric part of the ID
        new_id = last_id + 1
    else:
        new_id = 1

    formatted_id = f"{prefix}{new_id:04d}"  # Pad the ID with leading zeros to reach a total length of 9 digits
    return formatted_id


def extract_first_last_name(full_name):
    names = full_name.split()
    if len(names) >= 2:
        return names[0], ' '.join(names[1:])  # Handling cases where last name has spaces
    return full_name, ''  # If only one name is given, treat it as the first name


def validate_name(name):
    return len(name) >= 2 and name.isalpha() and name[0].isupper()


def validate_age(age):
    return age.isdigit() and 0 <= int(age) <= 100


def validate_gender(gender):
    return gender.upper() in ['M', 'F', 'O']


def validate_phone(phone):
    return re.match(r'^\d{3}-\d{3}-\d{4}$', phone)
