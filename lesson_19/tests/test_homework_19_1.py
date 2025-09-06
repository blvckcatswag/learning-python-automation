import requests
import pytest

URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
PARAMS = {"sol": 1000, "camera": "fhaz", "api_key": "DEMO_KEY"}


def test_api_status_code():
    """Проверяем, что API доступно и возвращает 200."""
    r = requests.get(URL, params=PARAMS)
    assert r.status_code == 200


def test_response_has_photos_key():
    """Убедимся, что в ответе есть ключ 'photos'."""
    r = requests.get(URL, params=PARAMS)
    data = r.json()
    assert "photos" in data


@pytest.mark.parametrize("param_key", ["sol", "camera", "api_key"])
def test_params_are_used(param_key):
    """Проверяем, что в словаре параметров есть нужные ключи."""
    assert param_key in PARAMS


def test_first_photo_has_img_src():
    """Проверяем, что хотя бы у первого фото есть ссылка 'img_src'."""
    r = requests.get(URL, params=PARAMS)
    data = r.json()
    photos = data.get("photos", [])
    assert photos, "Список фотографий пустой"
    first = photos[0]
    assert "img_src" in first
    assert first["img_src"].startswith("http")
