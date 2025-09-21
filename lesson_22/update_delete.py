from sqlalchemy.orm import Session
from models import engine, Student, Course, Enrollment


def update_student_name(old_name: str, new_name: str) -> bool:
    with Session(engine) as s:
        st = s.query(Student).filter_by(full_name=old_name).one_or_none()
        if not st:
            print("Студент не найден")
            return False
        st.full_name = new_name
        s.commit()
        print(f"OK: {old_name} -> {new_name}")
        return True


def update_course_title(old_title: str, new_title: str) -> bool:
    with Session(engine) as s:
        crs = s.query(Course).filter_by(title=old_title).one_or_none()
        if not crs:
            print("Курс не найден")
            return False
        crs.title = new_title
        s.commit()
        print(f"OK: {old_title} -> {new_title}")
        return True


def unenroll_student_from_course(student_name: str, course_title: str) -> int:
    with Session(engine) as s:
        st = s.query(Student).filter_by(full_name=student_name).one_or_none()
        crs = s.query(Course).filter_by(title=course_title).one_or_none()
        if not st or not crs:
            print("Студент или курс не найдены")
            return 0
        deleted = s.query(Enrollment).filter_by(student_id=st.id, course_id=crs.id).delete()
        s.commit()
        print(f"OK: {student_name} снят с курса {course_title} (удалено связей: {deleted})")
        return deleted


def delete_student(student_name: str) -> bool:
    with Session(engine) as s:
        st = s.query(Student).filter_by(full_name=student_name).one_or_none()
        if not st:
            print("Нет такого студента")
            return False
        s.delete(st)
        s.commit()
        print(f"OK: студент {student_name} удалён")
        return True


def delete_course(course_title: str) -> bool:
    with Session(engine) as s:
        crs = s.query(Course).filter_by(title=course_title).one_or_none()
        if not crs:
            print("Нет такого курса")
            return False
        s.delete(crs)
        s.commit()
        print(f"OK: курс {course_title} удалён")
        return True


if __name__ == "__main__":
    update_student_name("Guido Memasenko", "Guido van Meme")
    update_course_title("QA Automation", "QA & Automation")

    unenroll_student_from_course("Elliot Alderson", "Databases")

    delete_student("Guido van Meme")
    delete_course("QA & Automation")
