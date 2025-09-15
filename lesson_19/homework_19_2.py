import requests

BASE_URL = "http://127.0.0.1:8080"
FILENAME = "test.jpg"

with open(FILENAME, "rb") as f:
    resp = requests.post(f"{BASE_URL}/upload", files={"image": f})
print("POST /upload:", resp.status_code, resp.json())
assert resp.status_code == 201

resp = requests.get(f"{BASE_URL}/image/{FILENAME}", headers={"Content-Type": "text"})
print("GET /image:", resp.status_code, resp.json())
assert resp.status_code == 200
print("Image URL:", resp.json()["image_url"])

resp = requests.delete(f"{BASE_URL}/delete/{FILENAME}")
print("DELETE /delete:", resp.status_code, resp.json())
assert resp.status_code == 200
