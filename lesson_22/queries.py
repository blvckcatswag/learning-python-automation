from sqlalchemy import func
from sqlalchemy.orm import Session
from models import engine, Student, Course, Enrollment


def add_student_to_course(full_name: str, course_title: str):
    with Session(engine) as s:
        course = s.query(Course).filter_by(title=course_title).one_or_none()
        if course is None:
            course = Course(title=course_title)
            s.add(course)
            s.flush()
        st = Student(full_name=full_name)
        s.add(st)
        s.flush()
        s.add(Enrollment(student_id=st.id, course_id=course.id))
        s.commit()
        print(f"Добавлен {st} на курс {course.title!r}")


def students_by_course(course_title: str):
    with Session(engine) as s:
        crs = s.query(Course).filter_by(title=course_title).one_or_none()
        names = [st.full_name for st in (crs.students if crs else [])]
        print(f"Студенты курса {course_title}: {names}")
        return names


def courses_by_student(full_name: str):
    with Session(engine) as s:
        st = s.query(Student).filter_by(full_name=full_name).one_or_none()
        titles = [c.title for c in (st.courses if st else [])]
        print(f"Курсы студента {full_name}: {titles}")
        return titles


def rename_student(old: str, new: str):
    with Session(engine) as s:
        st = s.query(Student).filter_by(full_name=old).one_or_none()
        if not st: return print("Студент не найден")
        st.full_name = new
        s.commit()
        print(f"Переименован: {old} -> {new}")


def unenroll(full_name: str, course_title: str):
    with Session(engine) as s:
        st = s.query(Student).filter_by(full_name=full_name).one_or_none()
        crs = s.query(Course).filter_by(title=course_title).one_or_none()
        if not st or not crs: return print("Студент или курс не найдены")
        s.query(Enrollment).filter_by(student_id=st.id, course_id=crs.id).delete()
        s.commit()
        print(f"{full_name} снят с курса {course_title}")


def delete_student(full_name: str):
    with Session(engine) as s:
        st = s.query(Student).filter_by(full_name=full_name).one_or_none()
        if not st: return print("Нет такого студента")
        s.delete(st)
        s.commit()
        print(f"Удалён студент {full_name}")


def course_popularity():
    with Session(engine) as s:
        rows = (
            s.query(Course.title, func.count(Enrollment.student_id).label("cnt"))
            .join(Enrollment, Enrollment.course_id == Course.id)
            .group_by(Course.id)
            .order_by(func.count(Enrollment.student_id).desc())
            .all()
        )
        print("Популярность курсов:", rows)
        return rows


if __name__ == "__main__":
    # Примеры использования
    add_student_to_course("Guido Memasenko", "QA Automation")
    students_by_course("QA Automation")
    courses_by_student("Elliot Alderson")
    course_popularity()
    rename_student("Guido Memasenko", "Guido van Meme")
    unenroll("Guido van Meme", "QA Automation")
    delete_student("Guido van Meme")
