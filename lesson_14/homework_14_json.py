import json
import logging
from pathlib import Path

'''
Завдання 2:
Провалідуйте, чи усі файли у папці /work_with_json є валідними json. 
Pезультат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

Завдання 3:
Для файла /work_with_xml/groups.xml створіть функцію пошуку по group/number 
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
'''
LOG_FILE = "work_with_json/json__dzhevalov.log"

logger = logging.getLogger("json_format_logger")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def read_json(filename):
    data = None
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        logger.error(f"JSON-file {filename} invalid")
    return data

DIR_PATH = "work_with_json"
def get_all_json_files_from_dir(path):
    folder = Path(path)
    json_files_list = list(folder.glob("*.json"))
    return json_files_list

def json_format_checker(target_dir):
    all_json_files = get_all_json_files_from_dir(target_dir)
    for file in all_json_files:
        read_json(file)
    logging.shutdown()

json_format_checker(DIR_PATH)