import random
from sqlalchemy.orm import Session
from models import Base, engine, Student, Course, Enrollment

COURSES = ["Python Basic", "Databases", "QA Automation", "Algorithms", "Docker CI/CD"]
STUDENTS = [
    "Alex Mason", "Marina Light", "Elliot Alderson", "Angela Moss", "Tony Stark",
    "Bruce Wayne", "Clark Kent", "Peter Parker", "Diana Prince", "Barry Allen",
    "Neo Anderson", "Trinity", "Morpheus", "Dana Scully", "Fox Mulder",
    "Mike Ross", "Rachel Zane", "John Snow", "Arya Stark", "Hal Jordan"
]


def recreate_and_seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        courses = [Course(title=t) for t in COURSES]
        students = [Student(full_name=n) for n in STUDENTS]
        s.add_all(courses + students)
        s.flush()

        for st in students:
            for crs in random.sample(courses, k=random.randint(1, 3)):
                s.add(Enrollment(student_id=st.id, course_id=crs.id))
        s.commit()
    print("OK: база пересоздана")


if __name__ == "__main__":
    recreate_and_seed()
