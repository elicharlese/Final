from task_functions import *
from extra_credit import print_sorted_tasks

opt = None

while True:
    the_menu = {
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
    }
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
        "I": "incomplete tasks",
        "P": "incomplete tasks, sorted by priority",
        "D": "incomplete tasks, sorted by deadline"
    }
    priority_scale = {
        1: "Lowest",
        2: "Low",
        3: "Medium",
        4: "High",
        5: "Highest"
    }
    print_main_menu(the_menu)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters
    if opt not in the_menu:
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue
    print(f"You selected option {opt} to > {the_menu[opt]}.")
    if opt == 'q' or opt == 'Q':
        print("Goodbye!\n")
        break # exit the main `while` loop
    elif opt == 'L':
        if all_tasks == []:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue
        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_tasks(all_tasks, priority_scale)
        elif subopt == 'C':
            print_tasks(all_tasks, priority_scale, completed = 'yes')
        elif subopt == 'I':
            print_tasks(all_tasks, priority_scale, completed = 'no')
        elif subopt == 'P':
            print_sorted_tasks(all_tasks, priority_scale, sortby = 'priority')
        elif subopt == 'D':
            print_sorted_tasks(all_tasks, priority_scale, sortby = 'duedate')
        # Pause before going back to the main menu
    # ----------------------------------------------------------------
    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter each required field, separated by commas.")
            print("::: name, info, priority, MM/DD/YYYY, is task done? (yes/no)")
            new_task_list = input("> ")
            new_task_list = new_task_list.split(',')
            result = get_new_task(new_task_list, priority_scale)
            if type(result) == dict:
                all_tasks.append(result)
                print(f"Successfully added a new task!")
                print_task(result, ...)
            elif len(result) != 5:
                print(f"WARNING: invalid number of fields!")
                print(f"You provided {result}, instead of the expected 5.\n")
            else:
                print(f"WARNING: invalid task field: {result}\n")
            print("::: Would you like to add another task?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()
    # ----------------------------------------------------------------
    elif opt == 'U':
        continue_action = 'y'
        while continue_action == 'y':
            if all_tasks == []:
                print("WARNING: There is nothing to update!")
                break
            print("::: Which task would you like to update?")
            print_tasks(all_tasks, priority_scale, name_only = True, show_idx = True, start_idx = 1)
            print("::: Enter the number corresponding to the task.")
            user_option = input("> ")
            if is_valid_index(user_option, all_tasks, start_idx=1):
                idx = int(user_option) - 1
                subopt = get_selection("update", all_tasks[idx], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|")
                field_info = input("> ")
                result = update_task(all_tasks, user_option, priority_scale, subopt, field_info, start_idx = 1)
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")
                    print_task(result, priority_scale)
                else: # update_task() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")
                    print(f"The task was not updated.")
            else: # is_valid_index() returned False
                print(f"WARNING: |{user_option}| is an invalid task number!")
            print("::: Would you like to update another task?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()
    # ----------------------------------------------------------------
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            status = save_tasks_to_csv(all_tasks, filename) 
            if status == -1: 
                print(f"WARNING: |{filename}| is an invalid file name!")
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the tasks to |{filename}|")
    #--------------------------------------------------------------------------
    input("::: Press Enter to continue")
    continue

print("Have a nice day!")
# Back to top