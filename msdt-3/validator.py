import csv
import re

regex = {
    "telephone" : "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height"    : "^[0-2]\.\d{2}$",
    "inn"       : "^\d{12}$",
    "identifier": "^\d{2}-\d{2}\/\d{2}$",
    "occupation": "^[A-ZА-Я][A-Za-zА-Яa-я -]+$",
    "latitude"  : "^-?(1[0-7][0-9]|\d{1,2}|180)\.\d+$",
    "blood_type": "^(O|A|B|AB)[+−]$",
    "issn"      : "^\d{4}-\d{4}$",
    "uuid"      : "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    "date"      : "^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
}


def validate(row: dict) -> bool:
    """
        Проверяет соответствие строки регулярным выражениям
        .
        :param row: строка из файла CSV
        :return: True, если все поля прошли проверку; иначе False
    """
    for column, pattern in regex.items():
        if not re.match(pattern, row[column]):
            return False
    return True


def process_csv(n):
    """
        Проверяет соответствие строки регулярным выражениям
        .
        :param n: номер варианта
        :return: список номеров строк не прошедших проверку
    """
    invalid_rows = []
    with open(f'{n}.csv', newline='', encoding='utf-16') as file:
        reader = csv.DictReader(file, delimiter=';')
        next(reader)
        for row_number, row in enumerate(reader, start=0):
            if not validate(row):
                invalid_rows.append(row_number)
    return invalid_rows
