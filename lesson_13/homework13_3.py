import logging
from pathlib import Path
import xml.etree.ElementTree as ET

# Путь к XML-файлу
xml_file = Path(r"C:\Users\User.PC-475\Desktop\homework_task\work_with_xml\groups.xml")

# Путь к папке с домашкой
homework_folder = Path(r"C:\Users\User.PC-475\PycharmProjects\learning-python-automation\lesson_13")

# Лог-файл
log_file = homework_folder / "xml__masenko.log"

# Настройка логгера
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def find_incoming_by_group_number(group_number: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")
        if number is not None and number.text == group_number:
            incoming = group.find("timingExbytes/incoming")
            if incoming is not None:
                return incoming.text
    return None

if __name__ == "__main__":
    # Пример: ищем по номеру группы "1"
    number_to_find = "1"
    result = find_incoming_by_group_number(number_to_find)

    if result is not None:
        logging.info(f"Группа {number_to_find} — incoming: {result}")
        print(f"Группа {number_to_find} — incoming: {result}")
    else:
        logging.info(f"Группа {number_to_find} не найдена или нет incoming.")
        print(f"Группа {number_to_find} не найдена или нет incoming.")

    print(f"Проверка завершена. Лог: {log_file}")
