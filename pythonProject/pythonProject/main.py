"""
This is a Welcome Page
"""
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists
from sqlalchemy.orm.exc import NoResultFound

import hashlib
import re
from Student import student_manager
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String)

engine = create_engine('sqlite:///user_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class UserManagement():
    def __init__(self):
        # if os.path.exists('user_database.db'):
        #     os.remove('user_database.db')
        self.session=Session()

    def register_user(self):
        print('===========================Registration=============================')
        print('\u2666 Account Name is between 3 and 6 letters long')
        print('\u2666 Account name\'s first letter must be capitalized')
        while True:
            username = input("Enter a username: ")
            username_validity = self.is_valid_username(username)
            if username_validity == "invalid_format":
                print("\u274C Account Name Not Valid! Please follow the specified format.")
                continue
            elif username_validity == "exists":
                print("\u274C Registration Failed! Account Already Exists")
                print("\n===============================================\n")
                break

            print('\u2666 Password must start with one of the following special characters !@#$%^&*')
            print('\u2666 Password must contain at least one digit, one lowercase letter, and one uppercase letter')
            print('\u2666 Password is between 6 and 12 characters long')
            while True:
                password = input("Please Enter your password: ")
                if not self.is_valid_password(password):
                    print("\u274C Password Not Valid!")
                    continue

                hashed_password = hashlib.md5(password.encode()).hexdigest()
                new_user = User(username=username, password=hashed_password)
                try:
                    self.session.add(new_user)
                    self.session.commit()
                except IntegrityError:
                    print("\u274C Registration Failed!")
                    print("\n===============================================\n")
                    break

                print("\u2714 Registration Completed!")
                print('\n==========================================================\n')
                return

    def is_valid_username(self, username):
        if not re.match("^[A-Z][a-zA-Z]{2,5}$", username):
            return "invalid_format"
        if self.check_username_exists(username):
            return "exists"
        return True

    def check_username_exists(self, username):
        # Check if username already exists in the database
       return self.session.query(exists().where(User.username == username)).scalar()

    def is_valid_password(self, password):
        if not (6 <= len(password) <= 12):
            return False
        if not re.search("[A-Z]", password) or not re.search("[a-z]", password) or not re.search("[0-9]", password):
            return False
        if not password[0] in "!@#$%^&*":
            return False
        return True

    def login(self):
        print('=========================Login============================')
        while True:
            username = input("Please Enter Your Account: ")
            try:
                user = self.session.query(User).filter(User.username == username).one()
            except NoResultFound:
                print('\u274C Login Failed! Account Not Exists')
                break

            while True:
                password = input("Please Enter your password: ")
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if user.password != hashed_password:
                    print('\u274C Login Failed! Invalid Password')
                    continue
                student_manager.print_student_menu(username)
                break
            break


# Usage example
user_manager = UserManagement()

# Welcome page (content loaded from welcome.txt)
while True:
    with open("welcome.txt", "r") as file:
        welcome_content = file.read()
        print(welcome_content)
        choice = input("Please Enter(1-3):")
        if choice == '1':
            user_manager.login()
        elif choice == '2':
            user_manager.register_user()
        elif choice == '3':
            exit()
        else:
            print("Invalid choice. Please enter '1' or '2'.")
