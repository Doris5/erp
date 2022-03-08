def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    exit_message = "(0) Exit program"
    print(title + ":")
    for i in range(len(list_options)):
        print(f"({i + 1}) {list_options[i]}")
    print(exit_message)


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print(label + ":")
    if type(result) == float:
        print("{:.2f}".format(result))
    elif type(result) == dict:
        [print(f"{key}: {value}") for key, value in result.items()]
    elif type(result) == list:
        [print(items) for items in result]
    else:
        print(result)


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    max_cell_len = 30
    table_width = 1 + (max_cell_len + 3) * len(table[0])
    print(f"/{'-' * (table_width - 2)}\\")
    for line in table:
        # print list of lists as a table
        for cell in line:
            print("|", end="")
            print(str(cell).center(max_cell_len + 2), end="")
        print("|")
        # print inside borders after content lines if it's not the last line
        if line != table[len(table) - 1]:
            for _ in line:
                print(f"|{'-' * (max_cell_len + 2)}", end="")
            print("|")
    print(f"\\{'-' * (table_width - 2)}/")


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    return input(label)


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inputs = []

    for question in labels:
        answer = input(question)
        inputs.append(answer)

    return inputs


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"Error: {message}")


def test():
    print_table(
        [["id", "product", "type"],
         ["0", "Bazooka", "portable"],
         ["1", "Sidewinder", "missile"]])


if __name__ == "__main__":
    test()
