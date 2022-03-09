from ctypes import util

# from controller.hr import load_data

# from controller.util import generate_id
import terminal as view
import hr  # model
from util import generate_id

"""
#TODO Import model, view etc. didnt work right now
#TODO Switch max_cell_len = 25
#TODO display_menu(): options = Remove "Back to main menu"
# """


def switch_to_dictionary():
    data = []
    l_data = hr.load_data()
    for d in l_data:
        l_data_diciotnary = {
            "id": d[0],
            "name": d[1],
            "birthday": d[2],
            "department": d[3],
            "clearance": d[4],
        }
        data.append(l_data_diciotnary)
    return data


def list_employees():
    view.print_table(hr.add_headers_to_data())


def add_employee():
    id = generate_id()
    name = str(input("Enter the employee name: "))
    date_of_birth = str(input("Enter the date of birth: "))
    department = str(input("Enter the department name: "))
    clearance = str(input("Enter the clearance number: "))
    new_employee = [id, name, date_of_birth, department, clearance]
    hr.add_employee_to_csv(hr.add_employee_to_table(new_employee))


def update_employee():
    id = str(input("Enter the ID of employee to update: "))
    datas = hr.load_data()
    module_headers = ["Name: ", "Birth date: ", "Department: ", "Clearance: "]
    updated_table = hr.update(datas, id, module_headers)
    hr.add_employee_to_csv(updated_table)


def delete_employee():
    id = str(input("Enter the ID of employee to remove: "))
    datas = hr.load_data()
    hr.remove_employee(datas, id)


# TODO Problem with date 01-01-1111 cut zeros
def get_oldest_and_youngest():
    sort_header = "Sort by (o)ldest or (y)oungest: "
    input = view.get_input(sort_header).lower()
    if input == "o":
        oldest = hr.get_oldest_employee()
        view.print_table(hr.add_header_to_data(oldest))
    if input == "y":
        youngest = hr.get_youngest_employee()
        view.print_table(hr.add_header_to_data(youngest))


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = [
        "List employees",
        "Add new employee",
        "Update employee",
        "Remove employee",
        "Oldest and youngest employees",
        "Employees average age",
        "Employees with birthdays in the next two weeks",
        "Employees with clearance level",
        "Employee numbers by department",
    ]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != "0":
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)


if __name__ == "__main__":
    menu()
