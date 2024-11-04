from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base
import random

# connect to the PostgreSQL database
DATABASE_URL = "postgresql://dbaskak@localhost:5432/student_management"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# associative table for the many-to-many relationship between students and courses
enrollment_table = Table(
    'enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


# model for students
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # many-to-many relationship through the enrollments table
    courses = relationship("Course", secondary=enrollment_table, back_populates="students")


# model for courses
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # many-to-many relationship through the enrollments table
    students = relationship("Student", secondary=enrollment_table, back_populates="courses")


# create tables in the database
Base.metadata.create_all(engine)


# function to add courses and students
def populate_data():
    # add 5 courses
    courses = [Course(name=f"Course {i + 1}") for i in range(5)]
    session.add_all(courses)
    session.commit()

    # add 20 students and enroll them in random courses
    students = [Student(name=f"Student {i + 1}") for i in range(20)]
    for student in students:
        enrolled_courses = random.sample(courses, k=random.randint(1, 3))
        student.courses.extend(enrolled_courses)
        session.add(student)

    session.commit()


# function to add a new student and enroll them in a course
def add_student(name, course_id):
    student = Student(name=name)
    course = session.get(Course, course_id)  # используем session.get вместо query.get
    if course:
        student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"added {name} to {course.name}")

# function to get students enrolled in a specific course
def get_students_on_course(course_id):
    course = session.get(Course, course_id)  # используем session.get вместо query.get
    if course:
        print(f"students registered on {course.name}:")
        for student in course.students:
            print(f" - {student.name}")

# function to get courses a specific student is enrolled in
def get_courses_for_student(student_id):
    student = session.get(Student, student_id)  # используем session.get вместо query.get
    if student:
        print(f"courses registered for {student.name}:")
        for course in student.courses:
            print(f" - {course.name}")

# function to update a student's name
def update_student_name(student_id, new_name):
    student = session.get(Student, student_id)  # используем session.get вместо query.get
    if student:
        student.name = new_name
        session.commit()
        print(f"updated student name to {new_name}")

# function to delete a student
def delete_student(student_id):
    student = session.get(Student, student_id)  # используем session.get вместо query.get
    if student:
        session.delete(student)
        session.commit()
        print(f"deleted student {student.name}")


# calling functions for testing
populate_data()  # create and assign students and courses
add_student("New Student", 1)  # add a new student and enroll them in course with id=1
get_students_on_course(1)  # get all students in course with id=1
get_courses_for_student(1)  # get all courses that student with id=1 is enrolled in
update_student_name(1, "Updated Student")  # update name of student with id=1
delete_student(2)  # delete student with id=2
