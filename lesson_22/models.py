from __future__ import annotations
from typing import List
from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

DB_URL = "sqlite:///lesson22_school.db"
engine = create_engine(DB_URL, echo=False)


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    enrollments: Mapped[List["Enrollment"]] = relationship(back_populates="student", cascade="all, delete-orphan")
    courses: Mapped[List["Course"]] = relationship(secondary="enrollments", back_populates="students")

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name={self.full_name!r})"


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    enrollments: Mapped[List["Enrollment"]] = relationship(back_populates="course", cascade="all, delete-orphan")
    students: Mapped[List["Student"]] = relationship(secondary="enrollments", back_populates="courses")

    def __repr__(self) -> str:
        return f"Course(id={self.id}, title={self.title!r})"


class Enrollment(Base):
    __tablename__ = "enrollments"
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), primary_key=True)

    student: Mapped[Student] = relationship(back_populates="enrollments")
    course: Mapped[Course] = relationship(back_populates="enrollments")
