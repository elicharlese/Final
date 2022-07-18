import datetime
from task_system import *

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print("==========================")
    print("What would you like to do?")
    for key, value in menu.items():
        print(f"{key} - {value}")
    print("==========================")

def get_written_date(date_input):
    """
    Returns the date in the format:
    YYYY-MM-DD
    """
    date_input = date_input.split("-")
    return datetime.now().strftime("%Y-%m-%d")