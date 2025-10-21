# 29.1 Dockerizate everything

## Что проверено тестами
- Подключение к БД (Postgres)
- CRUD: insert / update / delete
- Select + list

## Как запустить
```bash
docker compose up -d db
docker compose run --rm app pytest -q
