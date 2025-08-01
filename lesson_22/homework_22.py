import random

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

db_name = 'school.db'

engine = create_engine(f'sqlite:///{db_name}', echo=False)

Base = declarative_base()

student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"Student(id= {self.id}, name= {self.name}, age= {self.age})"

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=student_course,  back_populates="courses")

    def __repr__(self):
        return f"Course(id= {self.id}, title= {self.title})"

def create_new_db():
    if not os.path.isfile(db_name):
        Base.metadata.create_all(engine)
        return True
    else:
        print("База вже створена")
        return False

# create_new_db()

Session = sessionmaker(bind=engine)
session = Session()

def fill_db_with_data():
    if create_new_db():
        course_titles = ["Math", "Physics", "Chemistry", "Biology", "Python"]
        courses = [Course(title=title) for title in course_titles]
        session.add_all(courses)
        session.commit()

        for i in range(1, 21):
            student = Student(name=f"Student {i}", age=random.randint(18, 25))
            enrolled_courses = random.sample(courses, k=random.randint(1, 5))
            student.courses.extend(enrolled_courses)
            session.add(student)

        session.commit()

    else:
        print("Початкові данні вже додані")


fill_db_with_data()


def add_student_with_courses(name, age, course_titles):
    found_courses = session.query(Course).filter(Course.title.in_(course_titles)).all()

    if not found_courses:
        print("Жодного курсу не знайдено.")
        return

    new_student = Student(name=name, age=age)
    new_student.courses.extend(found_courses)
    session.add(new_student)
    session.commit()

    course_list = ", ".join(course.title for course in found_courses)
    print(f"Студента {name} додано до курсів: {course_list}")

def get_student_by_name(name):
    return  session.query(Student).filter_by(name=name).first()

def get_students_by_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        print(f"Студенти на курсі '{course_title}':")
        for student in course.students:
            course_names = [c.title for c in student.courses]
            print(f"- {student.name}: {', '.join(course_names)}")
    else:
        print(f"Курс '{course_title}' не знайдено.")

def get_courses_by_student(student_name):
    student = get_student_by_name(student_name)
    if student:
        print(f"Курси для '{student.name}':")
        for course in student.courses:
            print(f"- {course.title}")
    else:
        print(f"Студента '{student_name}' не знайдено.")

def update_student_name(old_name, new_name):
    student = get_student_by_name(old_name)
    if student:
        student.name = new_name
        session.commit()
        print(f"Ім'я змінено: {old_name} → {new_name}")
    else:
        print(f"Студента '{old_name}' не знайдено.")

def delete_student_by_name(name):
    student = get_student_by_name(name)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студента '{name}' видалено.")
    else:
        print(f"Студента '{name}' не знайдено.")

add_student_with_courses("Василь Петренко", 22,["Math"])
add_student_with_courses("Семен Клопотенко", 20,["Python", "Math", "Chemistry"])

get_students_by_course("Math")
get_courses_by_student("Student 1")
get_courses_by_student("Василь Петренко")
print(get_student_by_name("Петро Клопотенко"))

update_student_name("Семен Клопотенко", "Петро Клопотенко")
print(get_student_by_name("Петро Клопотенко"))

delete_student_by_name("Петро Клопотенко")

students = session.query(Student).all()
print("Всі студенти та курси на які вони підписані:")
for s in students:
    print(f"{s.name}, {s.age}: {[c.title for c in s.courses]}")