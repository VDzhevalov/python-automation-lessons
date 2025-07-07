import logging
import xml.etree.ElementTree as ET

'''
Завдання 3:
Для файла /work_with_xml/groups.xml створіть функцію пошуку по group/number 
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
'''

logger = logging.getLogger("group_logger")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

TARGET_XML = "work_with_xml/groups.xml"

def find_incoming_by_group_number(xml_file_path, target_number):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number_elem = group.find('number')
        if number_elem is not None and number_elem.text == str(target_number):
            incoming_elem = group.find('timingExbytes/incoming')
            if incoming_elem is not None:
                logger.info(f"Group {target_number}: incoming = {incoming_elem.text}")
                return incoming_elem.text
            else:
                logger.info(f"Group {target_number} field doesn't exist timingExbytes/incoming")
                return None

    logger.info(f"Group {target_number} not present in file")
    return None

find_incoming_by_group_number(TARGET_XML, 6)