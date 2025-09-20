import logging
import os

import pytest
import requests
from requests.auth import HTTPBasicAuth

logger = logging.getLogger("cars_api_tests")
logger.setLevel(logging.INFO)

fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

file_handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
file_handler.setFormatter(fmt)
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt)
stream_handler.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

BASE_URL = os.getenv("CARS_API_URL", "http://127.0.0.1:8080")


@pytest.fixture(scope="class")
def auth_session():
    s = requests.Session()
    auth_url = f"{BASE_URL}/auth"

    username = os.getenv("CARS_API_USERNAME", "test_user")
    password = os.getenv("CARS_API_PASSWORD", "test_pass")

    logger.info("POST %s (basic auth)", auth_url)
    resp = s.post(auth_url, auth=HTTPBasicAuth(username, password), timeout=10)
    assert resp.status_code == 200, f"Auth failed: {resp.status_code} {resp.text}"

    token = resp.json().get("access_token")
    assert token, "В ответе нет access_token"
    s.headers.update({"Authorization": f"Bearer {token}"})
    logger.info("Токен получен, заголовок Authorization установлен")

    try:
        yield s
    finally:
        s.close()


def is_sorted(items, key):
    if not items:
        return True
    if key == "brand":
        values = [x["brand"] for x in items]
    else:
        values = [x[key] for x in items]
    return values == sorted(values)


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 10),
        ("engine_volume", 3),
        ("brand", 7),
        ("price", None),  # без limit -> все элементы
        ("year", 100),  # limit больше размера БД
    ],
)
class TestCarsSearch:
    def test_search_with_params(self, auth_session, sort_by, limit):
        url = f"{BASE_URL}/cars"
        params = {}
        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = str(limit)

        logger.info("GET %s params=%s", url, params)
        r = auth_session.get(url, params=params, timeout=10)

        logger.info("Status %s | %s bytes", r.status_code, len(r.content))
        assert r.status_code == 200, f"Ожидали 200, получили {r.status_code}"

        data = r.json()
        assert isinstance(data, list), "Ответ должен быть списком"

        total_db = 25
        expected_len = total_db if limit is None else min(limit, total_db)
        assert len(data) == expected_len, f"Ожидали {expected_len}, получили {len(data)}"

        assert is_sorted(data, sort_by), f"Список не отсортирован по {sort_by}"

        must = {"brand", "year", "engine_volume", "price"}
        for i, car in enumerate(data):
            assert must.issubset(car.keys()), f"Нет нужных полей в элементе #{i}: {car}"
