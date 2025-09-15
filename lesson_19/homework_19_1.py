import os
import requests

URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
PARAMS = {"sol": 1000, "camera": "fhaz", "api_key": "DEMO_KEY"}

def run(url=URL, params=PARAMS, limit=2, outdir="."):

    response = requests.get(url, params=params)
    data = response.json()
    photos = data["photos"]

    saved = []
    for i, photo in enumerate(photos[:limit], start=1):
        img_url = photo["img_src"]
        img_data = requests.get(img_url).content
        fname = os.path.join(outdir, f"mars_photo{i}.jpg")
        with open(fname, "wb") as f:
            f.write(img_data)
        saved.append(fname)
        print(f"Скачано: {fname}")
    return saved

if __name__ == "__main__":
    run()
