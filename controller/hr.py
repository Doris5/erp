""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

import data_manager, util

DATAFILE = "controller/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
# [["id", "product", "type"],
#  ["0", "Bazooka", "portable"],
#  ["1", "Sidewinder", "missile"]])


def load_data():
    return data_manager.read_table_from_file(DATAFILE)


def add_headers_to_data():
    return [HEADERS] + load_data()


# print(load_data())
# print(add_headers_to_data())
