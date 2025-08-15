import json
import logging
from pathlib import Path

# Папка с JSON для проверки
folder = Path(r"C:\Users\User.PC-475\Desktop\homework_task\work_with_json")

# Путь к папке с домашкой
homework_folder = Path(r"C:\Users\User.PC-475\PycharmProjects\learning-python-automation\lesson_13")

# Лог-файл по ТЗ
log_file = homework_folder / "json__masenko.log"

# Настройка логгера
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Проверка JSON-файлов
for file in folder.glob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.load(f)
    except Exception as e:
        logging.error(f"Файл {file.name} невалидный JSON: {e}")

print(f"Проверка завершена. Лог: {log_file}")
