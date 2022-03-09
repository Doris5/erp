""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

import data_manager, util
import terminal

DATAFILE = "controller/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
# [["id", "product", "type"],
#  ["0", "Bazooka", "portable"],
#  ["1", "Sidewinder", "missile"]])


def load_data():
    return data_manager.read_table_from_file(DATAFILE)


def add_employee_to_table(table):
    return load_data() + [table]


def add_employee_to_csv(table):
    data_manager.write_table_to_file(DATAFILE, table)


def add_headers_to_data():
    return [HEADERS] + load_data()


def collect_id(table):
    ids = []
    for row in table:
        ids.append(row[0])
    return ids


def update(table, id, headers_list):
    new_items = []
    ids = collect_id(table)
    if id in ids:
        new_items.append(id)
        new_elements = terminal.get_inputs(headers_list)
    for item in new_elements:
        new_items.append(item)
    for i in range(len(table)):
        if table[i][0] == id:
            table[i] = new_items
    return table


def remove_employee(table, id):
    ids = collect_id(table)
    if id in ids:
        for i in range(len(table)):
            if table[i][0] == id:
                table.pop(i)
                print(table)
                add_employee_to_csv(table)
                break


def get_oldest_employee():
    years = []
    oldest = 0
    oldest_employee = []
    datas = load_data()
    for i in datas:
        date_list_str = i[2].split("-")
        for i in range(len(date_list_str)):
            date_list_str[i] = int(date_list_str[i])
        years.append(date_list_str)
    oldest = min(years)
    for i in range(len(oldest)):
        oldest[i] = str(oldest[i])
    oldest = "-".join(oldest)
    for line in datas:
        if str(oldest) in line:
            oldest_employee.append(line)
    return oldest_employee


def get_youngest_employee():
    years = []
    youngest = 0
    youngest_employee = []
    datas = load_data()
    for i in datas:
        date_list_str = i[2].split("-")
        for i in range(len(date_list_str)):
            date_list_str[i] = int(date_list_str[i])
        years.append(date_list_str)
    youngest = max(years)
    for i in range(len(youngest)):
        youngest[i] = str(youngest[i])
    youngest = "-".join(youngest)
    print(youngest)
    for line in datas:
        if str(youngest) in line:
            youngest_employee.append(line)
    print(youngest_employee)
    return youngest_employee


def add_header_to_data(table):
    return [HEADERS] + table


# update(table, "45+ohJm&"dB", headers_list)
