import csv
import logging

'''
Завдання 1:
Візміть два файли з теки /work_with_csv порівняйте на наявність дублікатів і приберіть їх. 
Результат запишіть у файл result_<your_second_name>.csv
'''

logger = logging.getLogger("log_headers_info")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

CSV_FILE_FIRST = "work_with_csv/r-m-c.csv"
CSV_FILE_SECOND = "work_with_csv/rmc.csv"
CSV_FILE_THIRD = "work_with_csv/random.csv"
CSV_FILE_FOURTH = "work_with_csv/random-michaels.csv"

UNIQUE_ROWS_CSV = "work_with_csv/result_dzhevalov.csv"

def read_csv_rows(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        return header, [tuple(row) for row in reader]

def find_duplicates_in_csv(csv_data_first, csv_data_second):
    duplicate_rows = set(csv_data_first) & set(csv_data_second)
    logger.info(f"duplicate rows count = {duplicate_rows.__len__()}")
    return duplicate_rows

def find_unique_rows(csv_data_first, csv_data_second, duplicates):
    return list((set(csv_data_first) | set(csv_data_second)) - duplicates)


def write_csv(filename, header, rows):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def compare_and_delete_duplicate_from_csv(csv_first, csv_second):
    header1, csv_data_first = read_csv_rows(csv_first)
    header2, csv_data_second = read_csv_rows(csv_second)
    if header1 != header2:
        logger.warning("Header are not equals!")

    duplicates = find_duplicates_in_csv(csv_data_first, csv_data_second)
    unique_rows = find_unique_rows(csv_data_first, csv_data_second, duplicates)
    write_csv(UNIQUE_ROWS_CSV, header1, unique_rows)
    logging.shutdown()


compare_and_delete_duplicate_from_csv(CSV_FILE_FIRST, CSV_FILE_FOURTH)

