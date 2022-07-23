import datetime

all_tasks = [
        {
        "name": "Call XYZ",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
        },
        {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
        },
        {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority": 5,
        "duedate": '06/05/2022',
        "done": 'no'
        }
]

list_menu = {
        "A": "all tasks",
        "C": "completed tasks",
        "I": "incomplete tasks"
        }

priority_scale = {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
}

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

def get_written_date(date_input):  # TODO: Add function from labs
        """
        Returns the date in the format:
        YYYY-MM-DD
        """
        date_input = date_input.split("-")
        return datetime.now().strftime("%Y-%m-%d")

def get_selection(action, suboptions, to_upper=True, go_back=False): # TODO:: Fix the call from the main system
        """
        param: action (string) - the action that the user
                would like to perform; printed as part of
                the function prompt
        param: suboptions (dictionary) - contains suboptions
                that are listed underneath the function prompt.
        param: to_upper (Boolean) - by default, set to True, so
                the user selection is converted to upper-case.
                If set to False, then the user input is used
                as-is.
        param: go_back (Boolean) - by default, set to False.
                If set to True, then allows the user to select the
                option M to return back to the main menu

        The function displays a submenu for the user to choose from.
        Asks the user to select an option using the input() function.
        Re-prints the submenu if an invalid option is given.
        Prints the confirmation of the selection by retrieving the
        description of the option from the suboptions dictionary.

        returns: the option selection (by default, an upper-case string).
                The selection be a valid key in the suboptions
                or a letter M, if go_back is True.
        """
        print("::: What would you like to list? ")
        for key, value in suboptions.items():
                print(f"{key} - {value}")
        selection = input(":::: Enter your selection\n> ").upper()
        if go_back == False:
                if 'm' in suboptions or 'M' in suboptions:
                        print("Invalid submenu, which contains M as a key.")
                        return None
        while selection in suboptions:
                print(f"::: What would you like to {action.lower()}?")
                for key in suboptions:
                        print(f"{key} - {suboptions[key]}")
                if go_back == True:
                        selection = input(f"::: Enter your selection "
                                        f"or press 'm' to return to the main menu\n> ")
                else:
                        selection = input("::: Enter your selection\n> ")
                if to_upper:
                        selection = selection.upper()  # to allow us to input lower- or upper-case letters
                if go_back and selection.upper() == 'M':
                        return 'M'
                if to_upper:
                        print(f"You selected |{selection}| to",
                                f"{action.lower()} |{suboptions[selection].lower()}|.")
                else:
                        print(f"You selected |{selection}| to",
                                f"{action.lower()} |{suboptions[selection]}|.")
        return selection


def print_task(task, priority_map, name_only=False): # TODO:: Fix the call from the main system
        """
        param: task (dict) - a dictionary object that is expected
                to have the following string keys:
        - "name": a string with the task's name
        - "info": a string with the task's details/description
                (the field is not displayed if the value is empty)
        - "priority": an integer, representing the task's priority
        (defined by a dictionary priority_map)
        - "duedate": a valid date-string in the US date format: <MM>/<DD>/<YEAR>
                (displayed as a written-out date)
        - "done": a string representing whether a task is completed or not

        param: priority_map (dict) - a dictionary object that is expected
                to have the integer keys that correspond to the "priority"
                values stored in the task; the stored value is displayed for the
                priority field, instead of the numeric value.
        param: name_only (Boolean) - by default, set to False.
                If True, then only the name of the task is printed.
                Otherwise, displays the formatted task fields.

        returns: None; only prints the task values

        Helper functions:
        - get_written_date() to display the 'duedate' field
        """
        # def get_written_date(date_input):
        #     """
        #     Returns the date in the format:
        #     YYYY-MM-DD
        #     """
        #     date_input = date_input.split("-")
        #     return datetime.now().strftime("%Y-%m-%d")
        # if name_only:
        #         print(f"{task['name']}")
        # else:
        #         print(f"{task['name']}")
        #         print(f"{task['info']}")
        #         print(f"Priority: {priority_map[task['priority']]}")
        #         print(f"Due: {get_written_date(task['duedate'])}")
        #         print(f"Done: {task['done']}")
        #         print("==========================")


def print_tasks(task_list, priority_map, name_only=False,
                show_idx=False, start_idx=0, completed="all"): # TODO:: Fix the call from the main system
        """
        param: task_list (list) - a list containing dictionaries with
                the task data
        param: priority_map (dict) - a dictionary object that is expected
                to have the integer keys that correspond to the "priority"
                values stored in the task; the stored value is displayed
                for the priority field, instead of the numeric value.
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
        param: completed (str) - by default, set to "all".
                By default, prints all tasks, regardless of their
                completion status ("done" field status).
                Otherwise, it is set to one of the possible task's "done"
                field's values in order to display only the tasks with
                that completion status.

        returns: None; only prints the task values from the task_list

        Helper functions:
        - print_task() to print individual tasks
        """
        # print("-"*42)
        # for key in suboptions:  # go through all tasks in the list
        # if show_idx:  # if the index of the task needs to be displayed
        #         print(f"{...}.", end=" ")
        # if completed == "all":
        #         print_task(task, priority_map, name_only)
        # elif subopt == completed:
        #         print_task(task, priority_map, name_only)
