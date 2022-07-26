from task_functions import *
from task_system import *

list_menu = {
        "A": "all tasks",
        "C": "completed tasks",
        "I": "incomplete tasks",
        "P": "incomplete tasks, sorted by priority",
        "D": "incomplete tasks, sorted by deadline"
        }

def print_sorted_tasks(task_list, name_only = False, show_idx = False, start_idx = 0,
                sortby = "duedate", order = "asc"):
        """
        param: task_list (list) - a list containing dictionaries with
                the task data
        param: name_only (Boolean) - by default, set to False.
                If True, then only the name of the task is printed.
                Otherwise, displays the formatted task fields.
                Passed as an argument into the helper function.
        param: show_idx (Boolean) - by default, set to False.
                If False, then the index of the task is not displayed.
                Otherwise, displays the "{idx + start_idx}." before the
                task name.
        param: start_idx (int) - by default, set to 0;
                an expected starting value for idx that
                gets displayed for the first task, if show_idx is True.
        param: sortby (str) - by default, set to "duedate".
                By default, prints the incomplete tasks, displaying
                the raw "sortby" field first.
        param: order (str) - by default, set to "asc" (ascending).
                By default, prints the incomplete tasks, displaying
                the priority from the lowest to the highest keys.
        returns: the new sorted list (the original task_list is unmodified)
        """
        task_list = sorted(task_list, key = lambda x: x[sortby], reverse = (order == "desc"))
        return task_list