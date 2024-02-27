from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Create an engine to connect to the database (students.db)
engine = create_engine('sqlite:///students.db')  # Change echo=True to see SQL queries

# Create a base class to define the mapped classes
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    Major = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    score = relationship('Score', back_populates='student', cascade='all, delete-orphan')


    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, age={self.age}, gender={self.gender}, Major={self.Major}, phone={self.phone})>"


class Score(Base):
    __tablename__ = 'score'

    id = Column(String(9), ForeignKey('students.id'), primary_key=True)
    name = Column(String,nullable=False)
    CS1030 = Column(Integer, default=0)
    CS1100 = Column(Integer, default=0)
    CS2030 = Column(Integer, default=0)

    student = relationship('Student', back_populates='score')


# Create the engine to connect to the database

def create_database():
    engine = create_engine('sqlite:///students.db')  # Change echo=True to see SQL queries
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
