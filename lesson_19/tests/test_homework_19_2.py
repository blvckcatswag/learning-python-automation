import requests
import os

BASE_URL = "http://127.0.0.1:8080"
TEST_FILE = os.path.join(os.path.dirname(__file__), "test.jpg")
TEST_NAME = "test.jpg"


def test_upload_image():
    with open(TEST_FILE, "rb") as f:
        r = requests.post(f"{BASE_URL}/upload", files={"image": f})
    assert r.status_code == 201
    data = r.json()
    assert "image_url" in data
    assert data["image_url"].endswith(TEST_NAME)


def test_get_image_url():
    r = requests.get(f"{BASE_URL}/image/{TEST_NAME}",
                     headers={"Content-Type": "text"})
    assert r.status_code == 200
    data = r.json()
    assert "image_url" in data
    assert data["image_url"].endswith(TEST_NAME)


def test_delete_image():
    r = requests.delete(f"{BASE_URL}/delete/{TEST_NAME}")
    assert r.status_code == 200
    data = r.json()
    assert "message" in data
    assert TEST_NAME in data["message"]
