import pytest
import os
from lesson_11.homework_10 import log_event

LOG_FILE = "login_system.log"

@pytest.fixture(autouse=True)
def clear_log_file():
    """Очищает лог перед каждым тестом"""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w'):
            pass

@pytest.mark.parametrize(
    "username, status, expected_log",
    [
        ("user1", "success", "Login event - Username: user1, Status: success"),
        ("user2", "expired", "Login event - Username: user2, Status: expired"),
        ("user3", "failed", "Login event - Username: user3, Status: failed"),
        ("user4", "unknown", "Login event - Username: user4, Status: unknown"),
    ]
)
def test_log_written_to_file(username, status, expected_log):
    # Вызываем лог
    log_event(username, status)

    # Читаем лог-файл
    with open(LOG_FILE, 'r') as file:
        logs = file.read()

    # Проверяем, что нужная строка есть
    assert expected_log in logs
