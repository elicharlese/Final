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

def get_selection(action, suboptions, to_upper = True, go_back = False):
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
                option M to return back to the main menu.
        The function displays a submenu for the user to choose from.
        Asks the user to select an option using the input() function.
        Re-prints the submenu if an invalid option is given.
        Prints the confirmation of the selection by retrieving the
        description of the option from the suboptions dictionary.
        returns: the option selection (by default, an upper-case string).
                The selection be a valid key in the suboptions
                or a letter M, if go_back is True.
        """
        selection = None
        if go_back:
                if 'm' in suboptions or 'M' in suboptions:
                        print("Invalid submenu, which contains M as a key.")
                        return None
        while selection not in suboptions:
                print(f"::: What would you like to {action.lower()}?")
                for key in suboptions:
                        print(f"{key} - {suboptions[key]}")
                if go_back == True:
                        selection = input(f"::: Enter your selection "
                                                f"or press 'm' to return to the main menu\n> ")
                else:
                        selection = input("::: Enter your selection\n> ")
                if to_upper:
                        selection = selection.upper() # to allow us to input lower- or upper-case letters
                if go_back and selection.upper() == 'M':
                        return 'M'
        if to_upper:
                print(f"You selected |{selection}| to",
                        f"{action.lower()} |{suboptions[selection].lower()}|.")
        else:
                print(f"You selected |{selection}| to",
                        f"{action.lower()} |{suboptions[selection]}|.")
        return selection

is_valid_month = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
        }

is_valid_day = {
        "01": "Sunday",
        "02": "Monday",
        "03": "Tuesday",
        "04": "Wednesday",
        "05": "Thursday",
        "06": "Friday",
        "07": "Saturday",
        "08": "Sunday"
}

is_valid_year = {
        "2010": "2010",
        "2011": "2011",
        "2012": "2012",
        "2013": "2013",
        "2014": "2014",
        "2015": "2015",
        "2016": "2016",
        "2017": "2017",
        "2018": "2018",
        "2019": "2019",
        "2020": "2020",
        "2021": "2021",
        "2022": "2022"
}

def get_written_date(date_input):
        """
        Returns the date in the format:
        YYYY-MM-DD
        """
        month, day, year = date_input.split("/")
        return f"{month} {day}, {year}"

def print_task(task, priority_map, name_only=False):
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
        if name_only:
                print(f"{task['name']}")
        elif task['info'] != "":
                print(f"{task['name']}")
                print(f"* {task['info']}")
                print(f"* Due: {get_written_date(task['duedate'])}", end=' ')
                print(f"(Priority: {priority_map[task['priority']]})")
                print(f"* Completed? {task['done']}")
        else:
                print(f"{task['name']}")
                print(f"* Due: {get_written_date(task['duedate'])}", end=' ')
                print(f"(Priority: {priority_map[task['priority']]})")
                print(f"* Completed? {task['done']}")


def print_tasks(task_list, priority_map, name_only=False,
                show_idx=False, start_idx=0, completed="all"):
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
        print("-"*42)
        for task in task_list: # go through all tasks in the list
                if show_idx: # if the index of the task needs to be displayed
                        print(f"{task}.", end=" ")
                if completed == 'all': # if all tasks need to be displayed
                        print_task(task, priority_map, name_only)
                elif completed == 'yes':
                        print_task(task, priority_map, name_only)
                else:
                        print_task(task, priority_map, name_only)

def get_new_task(task_list, priority_map, name_only=False,
                show_idx=False, start_idx=0, completed="all"):
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

def is_valid_name(name):
        """
        param: name (str) - a string containing the task's name
        returns: True if the name is not empty, False otherwise
        """
        # if name != "":
        #         return True
        # else:
        #         return False
def  is_valid_priority(priority):
        """
        param: priority (int) - an integer representing the task's priority
        returns: True if the priority is between 1 and 5, False otherwise
        """
        # if priority in range(1, 6):
        #         return True
        # else:
        #         return False

def is_valid_date(date):
        """
        param: date (str) - a string containing the task's due date
        returns: True if the date is in the format YYYY-MM-DD, False otherwise
        """
        # if date.split("-")[0].isdigit() and date.split("-")[1].isdigit() and date.split("-")[2].isdigit():
        #         return True
        # else:
        #         return False

def is_valid_completion(completion):
        """
        param: completion (str) - a string containing the task's completion status
        returns: True if the completion status is either "done" or "not done", False otherwise
        """
        # if completion == "done" or completion == "not done":
        #         return True
        # else:
        #         return False

def is_valid_index(idx, in_list, start_idx = 0):
        """
        param: idx (str) - a string that is expected to
                contain an integer index to validate
        param: in_list - a list that the idx indexes
        param: start_idx (int) - by default, set to 0;
                an expected starting value for idx that
                gets subtracted from idx for 0-based indexing

        The function checks if the input string contains
        only digits and verifies that (idx - start_idx) is >= 0,
        which allows to retrieve an element from in_list.

        returns:
        - True, if idx is a numeric index >= start_idx
        that can retrieve an element from in_list.
        - False if idx is not a string that represents an
        integer value, if int(idx) is < start_idx,
        or if it exceeds the size of in_list.
        """
        if idx.isdigit() and (idx - start_idx) >= 0:
                idx = int(idx)
                if idx >= start_idx and idx < len(in_list):
                        return True
                else:
                        return False

def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
        """
        param: info_list - a list that contains task dictionaries
        param: idx (str) - a string that is expected to contain an integer
                index of an item in the input list
        param: start_idx (int) - by default is set to 0;
                an expected starting value for idx that gets subtracted
                from idx for 0-based indexing
        param: priority_map (dict) - a dictionary that contains the mapping
                between the integer priority value (key) to its representation
                (e.g., key 1 might map to the priority value "Highest" or "Low")
                Needed if "field_key" is "priority" to validate its value.
        param: field_key (string) - a text expected to contain the name
                of a key in the info_list[idx] dictionary whose value needs to
                be updated with the value from field_info
        param: field_info (string) - a text expected to contain the value
                to validate and with which to update the dictionary field
                info_list[idx][field_key]. The string gets stripped of the
                whitespace and gets converted to the correct type, depending
                on the expected type of the field_key.

        The function first calls one of its helper functions
        to validate the idx and the provided field.
        If validation succeeds, the function proceeds with the update
        return:
        If info_list is empty, return 0.
        If the idx is invalid, return -1.
        If the field_key is invalid, return -2.
        If validation passes, return the dictionary info_list[idx].
        Otherwise, return the field_key.

        Helper functions:
        The function calls the following helper functions:
        - is_valid_index()
        Depending on the field_key, it also calls:
        - is_valid_name()
        - is_valid_priority()
        - is_valid_date()
        - is_valid_completion()
        """

def delete_item(in_list, idx, start_idx = 0):
        """
        param: in_list - a list from which to remove an item
        param: idx (str) - a string that is expected to
                contain a representation of an integer index
                of an item in the provided list
        param: start_idx (int) - by default, set to 0;
                an expected starting value for idx that
                gets subtracted from idx for 0-based indexing

        The function first checks if the input list is empty.
        The function then calls is_valid_index() to verify
        that the provided index idx is a valid positive
        index that can access an element from info_list.
        On success, the function saves the item from info_list
        and returns it after it is deleted from in_list.

        returns:
        If the input list is empty, return 0.
        If idx is not of type string or start_idx is not an int, return None.
        If is_valid_index() returns False, return -1.
        Otherwise, on success, the function returns the element
        that was just removed from the input list.

        Helper functions:
        - is_valid_index()
        """
        if not in_list:
                return 0
        elif not isinstance(idx, str) or not isinstance(start_idx, int):
                return None
        elif not is_valid_index(idx, in_list, start_idx):
                return -1
        else:
                return in_list.pop(int(idx) - start_idx)

def load_tasks_from_csv(filename, in_list, priority_map):
        """
        param: filename (str) - A string variable that represents the
                name of the file from which to read the contents.
        param: in_list (list) - A list of task dictionary objects to which
                the tasks read from the provided filename is appended.
                If in_list is not empty, the existing tasks are not dropped.
        param: priority_map (dict) - a dictionary that contains the mapping
                between the integer priority value (key) to its representation
                (e.g., key 1 might map to the priority value "Highest" or "Low")
                Needed by the helper function.

        The function ensures that the last 4 characters of the filename are '.csv'.
        The function requires the `import csv` and `import os`.

        If the file exists, the function will use the `with` statement to open the
        `filename` in "read" mode. For each row in the csv file, the function will
        proceed to create a new task using the `get_new_task()` function.
        - If the function `get_new_task()` returns a valid task object,
                it gets appended to the end of the `in_list`.
        - If the `get_new_task()` function returns an error, the 1-based
                row index gets recorded and added to the NEW list that is returned.

        E.g., if the file has a single row, and that row has invalid task data,
        the function would return [1] to indicate that the first row caused an
        error; in this case, the `in_list` would not be modified.
        If there is more than one invalid row, they get excluded from the
        in_list and their indices will be appended to the new list that's
        returned.

        returns:
        * -1, if the last 4 characters in `filename` are not '.csv'
        * None, if `filename` does not exist.
        * A new empty list, if the entire file is successfully read from `in_list`.
        * A list that records the 1-based index of invalid rows detected when
        calling get_new_task().

        Helper functions:
        - get_new_task()
        """
        # if filename[-4:] != '.csv':
        #         return -1
        # elif not os.path.isfile(filename):
        #         return None
        # else:
        #         with open(filename, 'r') as f:
        #                 reader = csv.reader(f)
        #                 for row in reader:
        #                         task = get_new_task(row, priority_map)
        #                         if task:
        #                                 in_list.append(task)
        #                         else:
        #                                 NEW.append(reader.line_num)
        #         return NEW

def save_tasks_to_csv(tasks_list, filename):
        """
        param: tasks_list - The list of the tasks stored as dictionaries
        param: filename (str) - A string that ends with '.csv' which represents
                the name of the file to which to save the tasks. This file will
                be created if it is not present, otherwise, it will be overwritten.

        The function ensures that the last 4 characters of the filename are '.csv'.
        The function requires the `import csv`.

        The function will use the `with` statement to open the file `filename`.
        After creating a csv writer object, the function uses a `for` loop
        to loop over every task in the list and creates a new list
        containing only strings - this list is saved into the file by the csv writer
        object. The order of the elements in the list is:

        * `name` field of the task dictionary
        * `info` field of the task dictionary
        * `priority` field of the task as a string
        (i.e, "5" or "3", NOT "Lowest" or "Medium")
        * `duedate` field of the task as written as string
        (i.e, "06/06/2022", NOT "June 6, 2022")
        * `done` field of the task dictionary

        returns:
        -1 if the last 4 characters in `filename` are not '.csv'
        None if we are able to successfully write into `filename`
        """
        # if filename[-4:] != '.csv':
        #         return -1
        # else:
        #         with open(filename, 'w') as f:
        #                 writer = csv.writer(f)
        #                 for task in tasks_list:
        #                         writer.writerow([task['name'], task['info'], task['priority'], task['duedate'], task['done']])
        #         return None