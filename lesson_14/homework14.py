"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.

"""


class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        old_grade = self.average_grade
        self.average_grade = new_grade
        if new_grade > old_grade:
            print(f"{self.name} {self.surname} улучшил средний балл с {old_grade} до {new_grade}")
        elif new_grade < old_grade:
            print(f"{self.name} {self.surname} снизил средний балл с {old_grade} до {new_grade}")
        else:
            print(f"Средний балл {self.name} {self.surname} остался без изменений ({new_grade})")

    def display_info(self):
        print(f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}, Средний балл: {self.average_grade}")


student1 = Student(name="Aleksei", surname="Masenko", age=28, average_grade=80)

student1.display_info()

student1.update_average_grade(10)

student1.display_info()
