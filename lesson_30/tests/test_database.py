import time
import pytest
import allure
from src.database import Database

@allure.feature("Database")
@allure.story("Connection")
@allure.title("Подключение к PostgreSQL внутри docker-сети")
def test_connection():
    db = Database()
    for _ in range(30):
        if db.connect():
            break
        time.sleep(1)
    else:
        pytest.fail("DB is not available (timeout)")
    db.close()

@allure.feature("Database")
@allure.story("CRUD")
@allure.title("CRUD: insert → select → update → delete")
def test_insert_select_update_delete():
    db = Database()
    for _ in range(30):
        if db.connect():
            break
        time.sleep(1)
    else:
        pytest.fail("DB is not available")

    with allure.step("Готовим таблицу"):
        db.create_table()

    with allure.step("Вставка пользователя"):
        uid = db.insert_user("Bob", 25)

    with allure.step("Проверка выборки"):
        row = db.get_user(uid)
        assert row[1] == "Bob" and row[2] == 25

    with allure.step("Обновление возраста"):
        db.update_user_age(uid, 26)
        row2 = db.get_user(uid)
        assert row2[2] == 26

    with allure.step("Удаление и проверка отсутствия"):
        db.delete_user(uid)
        assert db.get_user(uid) is None

    db.close()

@allure.feature("Database")
@allure.story("Select")
@allure.title("Список пользователей на пустой таблице не падает")
def test_list_empty_ok():
    db = Database()
    for _ in range(30):
        if db.connect():
            break
        time.sleep(1)
    else:
        pytest.fail("DB is not available")

    db.create_table()
    with allure.step("Получение списка"):
        users = db.list_users()
        assert isinstance(users, list)
    db.close()
