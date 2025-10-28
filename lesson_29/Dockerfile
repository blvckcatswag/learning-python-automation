
FROM python:3.12-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY src ./src
COPY tests ./tests


CMD ["python", "-c", "print('Use: docker compose run --rm app pytest -q')"]
