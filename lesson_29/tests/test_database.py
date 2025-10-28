import time
import pytest
from lesson_29.src.database import Database

@pytest.fixture(scope="module")
def db():
    d = Database()
    # БД в контейнере может подниматься пару секунд
    for _ in range(30):
        if d.connect():
            break
        time.sleep(1)
    else:
        pytest.fail("Cannot connect to DB inside container")
    d.create_table()
    yield d
    d.close()

def test_connection(db):
    assert db.conn is not None

def test_insert_select_update_delete(db):
    uid = db.insert_user("Bob", 25)
    row = db.get_user(uid)
    assert row[1] == "Bob"
    assert row[2] == 25

    db.update_user_age(uid, 26)
    row2 = db.get_user(uid)
    assert row2[2] == 26

    db.delete_user(uid)
    assert db.get_user(uid) is None

def test_list_empty_ok(db):
    assert isinstance(db.list_users(), list)
