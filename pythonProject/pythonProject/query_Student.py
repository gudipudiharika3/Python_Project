

from Student_database import create_database, Student, Score


def query_student_scores():
    print("=============================== Student Scores ==========================")
    print("\u2666 1. Display Student Scores by Name ")
    print("\u2666 2. Update Student Scores by ID ")
    print("\u2666 3. Other Return")

    option = input("Enter your choice (1-3): ")
    if option == '1':
        display_student_scores_name()
    elif option == '2':
        update_scores_id()
    else:
        return


def display_student_scores_name():
    session = create_database()
    student_name = input("Enter student name to display scores: ")
    student_records = session.query(Student).filter_by(name=student_name).all()

    if student_records:
        print("========================== Student Records ==========================================")
        print(f"{'ID':<11}{'Name':<20}{'CS 1030':<8}{'CS 1100':<8}{'CS 2030':<8}")
        print('-' * 70)
        for student in student_records:
            for score in student.score:
                print(f"{student.id:<11}{student.name:<20}{score.CS1030:<8}{score.CS1100:<8}{score.CS2030:<8}")
    else:
        print("\u274C No student found with the given ID.")


def update_scores_id():
    student_id = input("Enter student ID to update scores: ")
    session = create_database()

    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        print(f"Updating scores for student ID {student_id}:")
        cs1030 = input("Enter new CS 1030 score (please Enter without modification):")
        if cs1030:
            while not cs1030.isdigit() or int(cs1030) < 0 or int(cs1030) > 100:
                print("Invalid CS 1030 score. Please enter a number between 0 and 100.")
                cs1030 = input("Enter new CS 1030 score (please Enter without modification): ")

            student_score = session.query(Score).filter_by(id=student_id).first()
            if not student_score:
                student_score = Score(id=student_id)

            student_score.CS1030 = int(cs1030)
            session.add(student_score)
            session.commit()

        cs1100 = input("Enter new CS 1100 score:(please Enter without modification):")
        if cs1100:
            while not cs1100.isdigit() or int(cs1100) < 0 or int(cs1100) > 100:
                print("Invalid CS 1100 score. Please enter a number between 0 and 100.")
                cs1100 = input("Enter new CS 1100 score (please Enter without modification): ")

            student_score = session.query(Score).filter_by(id=student_id).first()
            if not student_score:
                student_score = Score(id=student_id)

            student_score.CS1100 = int(cs1100)
            session.add(student_score)
            session.commit()

        cs2030 = input("Enter new CS 2030 score:(please Enter without modification):")
        if cs2030:
            while not cs2030.isdigit() or int(cs2030) < 0 or int(cs2030) > 100:
                print("Invalid CS 2030 score. Please enter a number between 0 and 100.")
                cs2030 = input("Enter new CS 2030 score (please Enter without modification): ")

            student_score = session.query(Score).filter_by(id=student_id).first()
            if not student_score:
                student_score = Score(id=student_id)

            student_score.CS2030 = int(cs2030)
            session.add(student_score)
            session.commit()
        display_student_scores_id(student_id)
        print("Scores updated successfully.")
    else:
        print("No student found with the given ID.")


def display_student_scores_id(student_id):
    session = create_database()

    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        print("========================== Student Records ==========================================")
        print(f"{'ID':<11}{'Name':<20}{'CS 1030':<8}{'CS 1100':<8}{'CS 2030':<8}")
        print('-' * 70)
        for score in student.score:
            print(f"{student.id:<11}{student.name:<20}{score.CS1030:<8}{score.CS1100:<8}{score.CS2030:<8}")
    else:
        print("\u274C No student found with the given ID.")